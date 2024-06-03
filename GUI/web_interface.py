# GUI/web_interface.py
from flask import Blueprint, render_template, request
from BLL.business_logic import UserLogic

# Khởi tạo blueprint cho giao diện người dùng
gui_blueprint = Blueprint('gui', __name__,template_folder='../GUI/templates/')

# Route để hiển thị form đăng nhập
@gui_blueprint.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Route để xử lý việc đăng nhập
@gui_blueprint.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user_logic = UserLogic()
    is_valid, message = user_logic.validate_user(username, password)

    if is_valid:
        return f"Đăng nhập thành công: {message}"
    else:
        return f"Đăng nhập thất bại: {message}"
