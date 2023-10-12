from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('')

@auth.route('/signup', methods= ['GET', 'POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(password, email, username)
        if len(password) < 7:
            flash('Make the password at least 7 characters long', category='error')
        else:
            flash('Account has been created', category='success')

    return render_template('sign_up.html')

