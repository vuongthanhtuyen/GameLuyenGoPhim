# GUI/web_interface.py
from flask import Blueprint, render_template, request

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

    if len(username) < 3:
        is_valid, message = False, "Tên đăng nhập quá ngắn"
    elif len(password) < 6:
        is_valid, message = False, "Mật khẩu quá ngắn"
    else:   
        is_valid, message = True, "Đăng nhập thành công"
    
    if is_valid:
        return f"Đăng nhập thành công: {message}"
    else:
        return f"Đăng nhập thất bại: {message}"
