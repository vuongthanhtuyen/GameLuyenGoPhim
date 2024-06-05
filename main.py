from GUI import create_app
# @app.route('/blog/<string:blog_id>')
# def blogpost(blog_id):
#     return "this is blog id " + blog_id
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
