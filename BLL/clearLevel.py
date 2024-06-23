from flask import Blueprint,flash, render_template, request, redirect, url_for
clearLevel_bl = Blueprint('clearLevel', __name__,template_folder='../GUI/templates/')


@clearLevel_bl.route('/clearLevel', methods=['GET','POST'])
def clearLevel():
    # flash('Note added!',category='success')
    if request.method=="POST":
        from DTO.models.Level_db import Level_db
        idLevel = int(request.form.get('idPost')) + 1
        level = Level_db.query.filter_by(id=idLevel).first()

    
    # return redirect(url_for('levelScreen.LevelScreenGet',idLevel= level.id, word_count = level.word_count))

    
    return render_template('levelScreen.html',idLevel = level.id, word_count = level.word_count)


