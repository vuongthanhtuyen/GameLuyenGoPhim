# main.py
from flask import Flask, render_template

from GUI.web_interface import gui_blueprint

app = Flask(__name__, template_folder='../TEST/GUI/templates/')

# Đăng ký blueprint cho giao diện người dùng
app.register_blueprint(gui_blueprint)


@app.route("/")
def home():
    return "Congrarulations, it's a web app! new"
@app.route("/index/")
def index():
    return render_template('index.html',name = "Thanh Tuyen xinh gai")
 
# @app.route('/blog/<string:blog_id>')
# def blogpost(blog_id):
#     return "this is blog id " + blog_id

if __name__ == '__main__':
    app.run(debug=True)
