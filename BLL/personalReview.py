from flask import Blueprint, render_template, flash

personalReview_bl = Blueprint('personalReview', __name__,template_folder='../GUI/templates/')


@personalReview_bl.route('/personalReview', methods=['GET'])
def personalReview():

    data_from_python = {'id': 1, 'recordWord': 500}
    # return render_template('index.html', data_from_python=data_from_python)

    return render_template('personalReview.html',data_from_python=data_from_python)

