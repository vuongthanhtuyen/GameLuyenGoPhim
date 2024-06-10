from flask import Blueprint, render_template, flash, redirect, url_for
from DTO.models.Level_db  import Level_db
from DTO.models.LeaderBoard_db  import LeaderBoard_db
from GUI import db
manageData_bl = Blueprint('manageData', __name__,template_folder='../GUI/templates/')


@manageData_bl.route('/manageData', methods=['GET'])
def manageData():
    levels = Level_db.query.all()
    return render_template('manageData.html', levels=levels) # trả về bảng level, truy cập vào: http://127.0.0.1:5000/manageDa

@manageData_bl.route('/seedData', methods=['GET'])
def seedData():
    for x in range(1,101):
        name_level = 'Level '+ str(x)
        if x < 2:
            pharse_count = 0
            word_count = x+3
        elif x < 21:
            pharse_count = x//2
            word_count = x*2+2
        elif x <100:
            pharse_count = (20+x)//4
        new_level = Level_db(name = name_level, phrase_count = pharse_count, word_count = word_count)
        db.session.add(new_level)
        db.session.commit()
    seedLeader()
    flash('SEED DATA thành công!',category='success')

    return redirect(url_for('home'))
# @manageData_bl.route("/levels/")
# def get_levels():
#     levels = Level.query.all()
#     levels_data = [{"id": level.id, "name": level.name, "pharseCount": level.pharseCount, "wordCount": level.wordCount, "date": level.date} for level in levels]
#     return jsonify(levels_data)


def seedLeader():
    new_leader = LeaderBoard_db(id_max_level =10,username ="Mít", total_words = 100, total_time = 1200)
    db.session.add(new_leader)
    db.session.commit()
    new_leader = LeaderBoard_db(id_max_level =15,username ="Dâu", total_words = 150, total_time = 3000)
    db.session.add(new_leader)
    db.session.commit()
    new_leader = LeaderBoard_db(id_max_level =12,username ="MeoMeo", total_words = 200, total_time = 1800)
    db.session.add(new_leader)
    db.session.commit()
    new_leader = LeaderBoard_db(id_max_level =14,username ="Cvat", total_words = 250, total_time = 2100)
    db.session.add(new_leader)
    db.session.commit()
    new_leader = LeaderBoard_db(id_max_level =14,username ="Cá", total_words = 300, total_time = 2400)
    db.session.add(new_leader)
    db.session.commit()



