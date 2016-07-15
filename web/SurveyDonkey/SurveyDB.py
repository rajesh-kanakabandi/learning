
import MySQLdb as mysql
import logging

logging.basicConfig(filename='db.log', level=logging.DEBUG)


class SurveyDB(object):
    def __init__(self):
        self.db = self.connect_db()

    def connect_db(self):
        return mysql.connect('mysql.server', 'codekiller', 'hello','codekiller$SD')

    def close(self):
        self.db.close()
    def _execute(self, sql, fetchone= False):
        '''this will execute all sql queries'''
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            if fetchone:
                data = cursor.fetchone()
            else:
                data = cursor.fetchall()
            logging.info("Query Success:" + sql)
            return data
        except Exception as e:
            logging.error("Error Querying:" + sql)
            logging.exception("Description: " +  str(e))
        return None

    def _update(self, sql, cursor = None):
        '''this will insert data to the table'''
        try:
            if not cursor:
                cursor = self.db.cursor()
            cursor.execute(sql)
            self.db.commit()
            logging.info('update successful: '+ sql)
            return True
        except Exception as e:
            logging.error("Error inserting data: "+sql)
            logging.exception("description:" + str(e))
        return False

    def get_user(self, uname = 'user1'):
        sql = """select id, uname, password from users where uname='%s'""" %(uname)
        user = self._execute(sql, True)
        if user:
            return {'id': int(user[0]), 'uname':user[1], 'password':user[2]}
        else:
            return None


    def login_user(self, uname, password):
        user = self.get_user(uname)
        if user and user['password']==password:
            print "User %s logged in" % uname
            return user
        else:
            print "User credentials invalid"
            return False

    def get_survey(self, sid):
        sql = """select id, sname from survey where id = %s """ % (sid)
        survey = self._execute(sql, True)
        return {'sid':survey[0], 'sname':survey[1]}



    def get_surveys(self,uid):
        sql = """select id, uid, sname from survey where uid = %s""" % (uid)
        rows = self._execute(sql)
        surveys = []
        for row in rows:
            if row:
                surveys.append({'id':int(row[0]), 'uid' : int(row[1]), 'sname': row[2] })
        return surveys

    def create_survey(self,uid, survey_name, cursor):
        sql = """insert into survey (uid, sname) values (%s, '%s')""" % (uid, survey_name)
        return self._update(sql, cursor)

    def save_survey(self, uid,data):
        cursor = self.db.cursor()
        if self.create_survey(uid,data['surveyName'], cursor):
            sid = cursor.lastrowid
            logging.info('saving survey for sid='+str(sid)+';')
            for question in data['questions']:
                db = self.connect_db()
                cursor = db.cursor()
                if self.add_question(sid, question['questionName'], cursor):
                    qid = cursor.lastrowid
                    for option in question['options']:
                        self.add_option(qid, option['optionName'])
                db.commit()
                db.close()
        return True


    def add_question(self, sid, question, cursor):
        sql = """insert into questions(sid, question) values (%s, '%s')""" % (sid, question)
        return self._update(sql, cursor)

    def add_option(self, qid, option):
        sql = """insert into options(qid, optiontitle, count) values (%s,'%s', 0)""" % (qid, option)
        return self._update(sql)

    def get_survey_questions(self,sid):
        questions = self.get_questions(sid)
        for question in questions:
            options = self.get_options(question['qid'])
            question['options']=options
        return questions

    def get_questions(self, sid):
        sql ="""select id, question from questions where sid =%s""" % (sid)
        rows = self._execute(sql)
        questions = [{'qid':row[0], 'questionName':row[1]} for row in rows]
        return questions

    def get_options(self, qid):
        sql ="""select id, optiontitle, count from options where qid =%s""" % (qid)
        rows = self._execute(sql)
        options = [{'oid':row[0], 'optionName':row[1], 'count':row[2]} for row in rows]
        return options

    def save_results(self,quesOptDicts):
        for question in quesOptDicts:
            oid = question[question.keys()[0]]
            qid = question.keys()[0]

            sql ="""update options set count = count+1 where id =%s and qid =%s""" % (oid, qid)
            self._update(sql)
        return

    def del_survey(self, sid):
        sql = """delete from survey where id = %s""" % sid
        self._update(sql)

    def del_questionAndOptions(self, qid):
        sql1 = """delete from questions where id = %s""" % qid
        sql2 = """delete from options where qid = %s""" % qid
        self._update(sql1)
        self._update(sql2)


    def remove_survey(self, sid):
        questions = self.get_questions(sid)
        self.del_survey(sid)
        for question in questions:
            self.del_questionAndOptions(question['qid'])


#sdb= SurveyDB()
#sdb.create_survey(sdb.get_user('user1'), 'first survey')
#sdb.add_question(1,'question 1 dont answer it')
#print sdb.get_surveys(sdb.get_user('user1'))