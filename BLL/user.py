from flask import Blueprint, render_template, request, flash, redirect, url_for
from DTO.models.User import User_db
from GUI import db ## nghĩa là from __init__.py inport db
from flask_login import login_user, login_required, logout_user, current_user

user_bl = Blueprint('user', __name__,template_folder='../GUI/templates/user/')

# thiết lập route để chỏ đến trang loginin
@user_bl.route('/login', methods=['GET', 'POST']) # methods post để gửi request lên server
def login():

    if request.method =="POST":
        email =  request.form.get('email')
        password = request.form.get('password')
        user = User_db.query.filter_by(email = email).first()
        if user:
            if user.password==password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    # data = request.form #Lấy dữ liệu trong form gửi đến
    # print(data)


    return render_template("login.html", user = current_user)

@user_bl.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home')) #trả về file auth.login

@user_bl.route('/sign_up',methods=['GET', 'POST'])
def sign_up():
    if request.method =="POST":
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')


        user = User_db.query.filter_by(email = email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(email)<4:
            flash('Email must be greater than 3 characters.', category='error')
            pass
        elif len(first_name) <1: 
            flash('First Name must be greater than or equal 1 characters.', category='error')
            pass
        elif password1 != password2:
            flash('Passwords dont\'t match.', category='error')
            pass
        else: 
            new_user = User_db(email=email, first_name=first_name, password=password1)
            db.session.add(new_user) #Thêm user vào database
            db.session.commit() # Lưu thay đổi trên database
            login_user(new_user, remember=True)

            flash('Account created!', category='success')
            return redirect(url_for('home')) # chuyển hướng về lại home, nhớ import redirect and url_for


    return render_template("sign_up.html",user=current_user)
