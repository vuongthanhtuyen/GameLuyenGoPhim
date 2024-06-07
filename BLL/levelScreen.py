from flask import Blueprint, render_template
levelScreen_bl = Blueprint('levelScreen', __name__,template_folder='../GUI/templates/')


@levelScreen_bl.route('/levelScreen', methods=['GET'])
def levelScreen():
    return render_template('levelScreen.html')


