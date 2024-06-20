from flask import Blueprint, render_template, flash
from GUI import db
from datetime import date



levelScreen_bl = Blueprint('levelScreen', __name__,template_folder='../GUI/templates/')


@levelScreen_bl.route('/levelScreen', methods=['GET'])
def levelScreen():
    return render_template('levelScreen.html')

@levelScreen_bl.route('/endGame', methods=['GET'])
def endGame():
    id_max_level = 22
    username = 'Me'
    total_words = 400
    total_time = 2000
    update_lowest_level(username,id_max_level,total_time,total_words)
    from DTO.models.LeaderBoard_db import LeaderBoard_db

    leader_boards = LeaderBoard_db.query.order_by(
        LeaderBoard_db.id_max_level.desc(),
        LeaderBoard_db.total_words.desc(),
        LeaderBoard_db.total_time.desc()
    ).limit(5).all()
    return render_template('leaderBoard.html', leader_boards=leader_boards)

def update_lowest_level( new_username, new_id_max_level,new_total_time, new_total_words ):
    from DTO.models.LeaderBoard_db import LeaderBoard_db
    level_count = LeaderBoard_db.query.count()

    if level_count < 5:
        # Nếu số lượng bản ghi ít hơn 5, thêm mới bản ghi
        new_leaderBoard = LeaderBoard_db(
            id_max_level = new_id_max_level,
            username = new_username,
            total_words = new_total_words,
            total_time = new_total_time
        )
        db.session.add(new_leaderBoard)
        db.session.commit()
        flash('Thêm mới một Top!',category='success')

    else:
        # Nếu đã có đủ 5 bản ghi, kiểm tra và cập nhật bản ghi thấp nhất
        lowest_leaderboard = LeaderBoard_db.query.order_by(
            LeaderBoard_db.id_max_level.asc(),
            LeaderBoard_db.total_words.asc(),
            LeaderBoard_db.total_time.asc()
        ).first()

    if lowest_leaderboard:
        if (new_id_max_level > lowest_leaderboard.id_max_level) or (
                (new_id_max_level == lowest_leaderboard.id_max_level) and (new_total_words > lowest_leaderboard.total_words)) or (
                (new_id_max_level == lowest_leaderboard.id_max_level) and (new_total_words == lowest_leaderboard.total_words) and (
                new_total_time > lowest_leaderboard.total_time)):
            lowest_leaderboard.id_max_level = new_id_max_level
            lowest_leaderboard.username = new_username
            lowest_leaderboard.total_words = new_total_words
            lowest_leaderboard.total_time = new_total_time
            db.session.commit()
            flash(f'CHÚC MỪNG BẠN ĐẠT TOP {new_id_max_level}', category='success')
        else:
            flash('KHÔNG LỌT TOP', category='success')
