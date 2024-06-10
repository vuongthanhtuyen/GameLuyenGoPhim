from flask import Blueprint,flash, render_template, request
clearLevel_bl = Blueprint('clearLevel', __name__,template_folder='../GUI/templates/')


@clearLevel_bl.route('/clearLevel', methods=['GET'])
def clearLevel():
    # flash('Note added!',category='success')

    return render_template('clearLevel.html',level = "1", time = "00:01:59")


