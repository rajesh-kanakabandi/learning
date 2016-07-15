
# A very simple Flask Hello World app for you to get started with...
import json
from flask import *
from flask_mail import Mail, Message
from functools import wraps
from SurveyDB import SurveyDB as sddb
import logging

app = Flask(__name__)
app.secret_key = 'needed to use session'

# mail = Mail(app)
# app.config.from_object(__name__)
# app.config.from_envvar('MINITWIT_SETTINGS', silent=True)
# app.config.update(
#     DEBUG = True,
#     MAIL_SERVER = 'smtp.gmail.com',
#     MAIL_PORT = 587,
#     MAIL_USE_TLS = True,
#     MAIL_USE_SSL = False,
#     MAIL_USERNAME ='surveydonkey.donotreply@gmail.com',
#     MAIL_PASSWORD ='surveys123',
#     DEFAULT_MAIL_SENDER = 'surveydonkey.donotreply@gmail.com'
#     )
# mail = Mail(app)

@app.route('/')
def home():
    return render_template('login.pt', logged_in=False)

def sessionIsValid(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session and 'uid' in session:
            return test(*args, **kwargs)
        else:
            return render_template('login.pt', logged_in=False, error="You need to login first.")
    return wrap

@app.route('/logout')
@sessionIsValid
def logout():
    session.pop('logged_in')
    session.pop('uid')
    return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method =='POST':
        #logic to authenticate
        db = sddb()
        user = db.login_user(request.form['uname'], request.form['password'])
        db.close()
        if user:
            session['logged_in'] = True
            session['uid']= user['id']
            session['uname']=user['uname']
            return redirect('/surveys')
        else:
            error = "Invalid Credentials. Please try again."

    return render_template('login.pt', logged_in=False, error=error)


@app.route('/surveys')
@sessionIsValid
def surveys():
    db = sddb()
    surveys = db.get_surveys(session['uid'])
    db.close()
    return render_template('surveys.pt', logged_in=True, user = session['uname'],surveys= surveys)

@app.route('/add')
@sessionIsValid
def make_new_survey():
    return render_template('new_survey.pt', logged_in=True,user = session['uname'])

@app.route('/view', methods=['GET', 'POST'])
def survey():
    if request.method =='POST':
        logging.info("form data = " + str(request.form))
        questionOptionDict = [{key:request.form[key]} for key in request.form.keys()]
        logging.info("form data dict: " + str(questionOptionDict))
        db = sddb()
        db.save_results(questionOptionDict)
        db.close()
        return redirect('/login')
    elif request.method == 'GET':
        sid = request.args.get('sid','')
        if sid:
            db= sddb()
            survey = db.get_survey(int(sid))
            questions = db.get_survey_questions(sid)
            db.close()
            logging.info(str(questions))
            return render_template('survey.pt', logged_in = False,
                        surveyName = survey['sname'], questions = questions, preview=False)
        else:
            return redirect('/login')

@app.route('/preview', methods=['GET'])
@sessionIsValid
def preview():

    if request.method == 'GET':
        sid = request.args.get('sid','')
        if sid:
            db= sddb()
            survey = db.get_survey(int(sid))
            questions = db.get_survey_questions(sid)
            db.close()
            logging.info(str(questions))
            return render_template('survey.pt', logged_in = True,user = session['uname'],
                        surveyName = survey['sname'], questions = questions, preview=True)
        else:
            return redirect('/surveys')

@app.route('/results', methods=['GET'])
@sessionIsValid
def results():

    if request.method == 'GET':
        sid = request.args.get('sid','')
        if sid:
            db= sddb()
            survey = db.get_survey(int(sid))
            questions = db.get_survey_questions(sid)
            db.close()
            logging.info(str(questions))
            return render_template('result.pt', logged_in = True,user = session['uname'],
                        surveyName = survey['sname'], questions = questions, preview=True)
        else:
            return redirect('/login')

@app.route('/save',methods=['POST'])
@sessionIsValid
def save():

    try:
        data = json.loads(request.data)
        db = sddb()
        db.save_survey(session['uid'], data)
        db.close()

    except Exception as e:
        logging.error(str(e))

    return "success"

@app.route('/share',methods=['GET', 'POST'])
@sessionIsValid
def share():
    if request.method=='POST':
        sid = request.form['sid']
        addresslist = request.form['addresslist'].replace(' ','').split(',')
        logging.info("sid = "+ str(sid))
        logging.info("addresses = "+ str(addresslist))
        # do some crazy smtp stuff
        msg = Message("Survey Donkey",
                    sender = ("Survey Donkey","surveydonkey.donotreply@gmail.com"),
                    recipients=addresslist)
        msg.body = """Hello,
                    You have been nomitated to take the followinf survey at Survey Donkey.
                    Please use the link below to complete the survey.

                    codekiller.pythonanywhere.com/view?sid=%s

                    We appreciate your time and effort.
                    --Survey Donkey.""" % (str(sid))
        #mail.send(msg)

        return redirect('/surveys')
    else:
        sid = request.args.get('sid','')
        return render_template('share.pt', logged_in = True,user = session['uname'],
                        sid = sid)


@app.route('/delete',methods=['GET'])
@sessionIsValid
def delete():
    try:
        sid = request.args.get('sid', '')
        if sid:
            db = sddb()
            db.remove_survey(sid)
            db.close()
    except Exception as e:
        logging.error("Could not remove survey %s description %s" % (sid, str(e)))
    return redirect('/surveys')
