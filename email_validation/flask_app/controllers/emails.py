from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.email import Email


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create')
def create():
    print(request.form)
    Email.save(request.form)
    return redirect('/')


@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_user(request.form):
        # we redirect to the template with the form.
        return redirect('/')
    # ... do other things
    Email.save(request.form)
    return redirect('/')