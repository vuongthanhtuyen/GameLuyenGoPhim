from flask import Blueprint, render_template, flash, redirect, url_for
from DTO.models.LeaderBoard_db  import LeaderBoard_db
from GUI import db
leaderBoard_bl = Blueprint('leaderBoard', __name__,template_folder='../GUI/templates/')


@leaderBoard_bl.route('/leaderBoard', methods=['GET'])
def leaderBoard_Get():
    leader_boards = LeaderBoard_db.query.order_by(
        LeaderBoard_db.id_max_level.desc(),
        LeaderBoard_db.total_words.desc(),
        LeaderBoard_db.total_time.desc()
    # ).limit(5).all()
    ).all()
    return render_template('leaderBoard.html', leader_boards=leader_boards)

