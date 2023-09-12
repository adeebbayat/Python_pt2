from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.login import Login
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    data = {
        "username": request.form['email'],
        "password" : pw_hash
    }
    # Call the save @classmethod on User
    user_id = Login.save(data)
    # store user id into session
    session['login_id'] = user_id
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    login_in_db = Login.get_by_login(data)
    # user is not registered in the db
    if not login_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(login_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['login_id'] = login_in_db.id
    # never render on a post!!!
    return redirect("/dashboard")
