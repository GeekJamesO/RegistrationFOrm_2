from flask import Flask, flash, redirect, render_template, request, session
import re
from datetime import date, datetime

app = Flask(__name__)
app.secret_key = "99bottlesorBeerOnThewall..."

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    session['email']= ''
    session['first_name']= ''
    session['last_name']= ''
    session['birthdate']= ''
    session['password1']= ''
    session['password2']= ''

    return render_template('success.html')

@app.route('/process', methods=['POST'])
def process():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    IsValid = True

    if len(request.form['email']) == 0:
        IsValid = False
        flash("Email: This cannot be blank.", "error")
    elif not EMAIL_REGEX.match(request.form['email']):
        IsValid = False
        flash("Email: You must pass a valid email address.", "error")
    else:
        session['email']=request.form['email']

    if len(request.form['first_name']) == 0:
        IsValid = False
        flash("First Name: This cannot be blank.", "error")
    else:
        for char in request.form['first_name']:
            if char.isdigit():
                IsValid = False
                flash("First Name: Names cannot contain numbers.", "error")
                break;
    session['first_name']=request.form['first_name']


    if len(request.form['last_name']) == 0:
        IsValid = False
        flash("Last Name: This cannot be blank.", "error")
    else:
        for char in request.form['last_name']:
            if char.isdigit():
                IsValid = False
                flash("Last Name: Names cannot contain numbers.", "error")
                break;
    session['last_name']=request.form['last_name']

    if len(request.form['birthdate']) == 0:
        isValid = False
        flash("Birthdate must not be empty!", "error")
    else:
        session['birthdate']=request.form['birthdate']

    if len(request.form['password1']) < 8:
        IsValid = False
        flash("Password: must be more than 8 characters.", "error")

    if len(request.form['password2']) < 8:
        IsValid = False
        flash("Confirm Password: must be more than 8 characters.", "error")

    if request.form['password1'] != request.form['password2']:
        IsValid = False
        flash("Passwords do not match each other.", "error")
    else:
        session['password1']=request.form['password1']
        session['password2']=request.form['password2']

    if (IsValid):
        return redirect('/success')
    else:
        return redirect('/index')

app.run(debug=True)
