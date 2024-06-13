from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user



db = SQLAlchemy() #khai báo database

DB_NAME = "database.db" # khai báo tên database


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thanhtuyen' # Liên quan gì đó đến tạo form
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #  Thiết lập cấu hình để kết nối với CSDL, và lưu ở dự án
    db.init_app(app) # nói với app database mình sử dụng 

    from DTO.models.Level_db import Level_db
    from DTO.models.LeaderBoard_db import LeaderBoard_db
    from DTO.models.User import User_db
    create_database(app)

    # app = Flask(__name__, template_folder='../TEST/GUI/templates/')

    # Đăng ký blueprint cho giao diện người dùng
    from BLL.clearLevel import clearLevel_bl
    from BLL.levelScreen import levelScreen_bl
    from BLL.manageData import manageData_bl
    from BLL.leaderBoard import leaderBoard_bl
    from BLL.user import user_bl
    # app.register_blueprint(gui_blueprint,)

    app.register_blueprint(clearLevel_bl, url_prefix='/')
    app.register_blueprint(levelScreen_bl, url_prefix='/')
    app.register_blueprint(manageData_bl, url_prefix='/')
    app.register_blueprint(leaderBoard_bl, url_prefix='/')
    app.register_blueprint(user_bl, url_prefix='/')

    @app.route("/")
    def home():
        return render_template('home.html', user = current_user)

    login_manager = LoginManager()
    login_manager.login_view = 'user.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User_db.query.get(int(id))
    

    
    return app
def create_database(app):
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')
