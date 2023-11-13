from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from .models import User, Post
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password: #als hash gebruikt: check_password_hash(user.password, password)
                flash('You have Logged in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('view.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('username does not exist.', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods= ['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        usermail = User.query.filter_by(email=email).first()
        print(password, email, username)
        if user:
            flash('This username already exists!', category='error')
        elif usermail:
            flash('This email has already been used.', category='error')
        elif len(password) < 7:
            flash('Make the password at least 7 characters long', category='error')
        else:
            new_user = User(email=email, username=username, password=password, credit=100) #If we want to encrypt the password in the database replace password=generate_password_hash(password, method="sha256")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account has been created', category='success')
            return redirect(url_for('view.home'))
            

    return render_template('sign_up.html', user=current_user)
