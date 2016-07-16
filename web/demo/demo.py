from flask import *
app = Flask(__name__)
users = [ ]
users.append({"name": "rajesh", "type": "admin", 'password': 'rajesh'})
users.append({"name": "madhavi", "type": "user", 'password': 'madhavi'})
users.append({"name": "priyanka", "type": "user", 'password': 'priyanka'})

@app.route("/")
def home():
    return render_template('login.pt')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        uname = request.form['uname']
        password = request.form['password']
        for user in users:
            if user['name'] == uname and user['password'] == password:
                return "Welcome {}".format(uname)

    return render_template('login.pt')

@app.route('/users')
def users_list():
    return render_template('users.pt', users=users)


if __name__ == "__main__":
    app.run(debug=True)
