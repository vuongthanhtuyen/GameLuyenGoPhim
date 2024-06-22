from flask import Blueprint,flash, render_template, request
clearLevel_bl = Blueprint('clearLevel', __name__,template_folder='../GUI/templates/')


@clearLevel_bl.route('/clearLevel', methods=['GET','POST'])
def clearLevel():
    # flash('Note added!',category='success')
    if request.method=="POST":

        idLevel = int(request.form.get('idPost'))
        word_count = int(request.form.get('wordCountPost'))
    


    return render_template('levelScreen.html',idLevel = idLevel, word_count = word_count)


