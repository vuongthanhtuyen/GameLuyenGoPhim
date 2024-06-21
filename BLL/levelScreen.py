from flask import Blueprint,request, render_template, flash, url_for,redirect, session
from GUI import db
from datetime import date
from flask_login import current_user




levelScreen_bl = Blueprint('levelScreen', __name__,template_folder='../GUI/templates/')



@levelScreen_bl.route('/levelScreen', methods=['GET', 'POST'])
def LevelScreen():
    if request.method=="POST":
        from DTO.models.LeaderBoard_db import LeaderBoard_db
        level_count = LeaderBoard_db.query.count()
        topUser = LeaderBoard_db(
            id_max_level = 21,
            username = "",
            total_words = 299,
            total_time = 32
        )

        #check top 5
        lowest_leaderboard = LeaderBoard_db.query.order_by(
            LeaderBoard_db.id_max_level.desc(),
            LeaderBoard_db.total_words.desc(),
            LeaderBoard_db.total_time.desc()
        ).offset(4).limit(1).first()


        session["createUsername"] = topUser
        if level_count < 5:
        # Nếu số lượng bản ghi ít hơn 5, thêm mới bản ghi
            return redirect(url_for("levelScreen.CreateUsername"))

        elif lowest_leaderboard:
            if (topUser.id_max_level > lowest_leaderboard.id_max_level) or (
                    (topUser.id_max_level == lowest_leaderboard.id_max_level) and (topUser.total_words > lowest_leaderboard.total_words)) or (
                    (topUser.id_max_level == lowest_leaderboard.id_max_level) and (topUser.total_words == lowest_leaderboard.total_words) and (
                    topUser.total_time > lowest_leaderboard.total_time)):
                #nếu user đạt top thì add vào một thằng mới
                return redirect(url_for("levelScreen.CreateUsername"))
        session.pop("createUsername",None)
        return redirect(url_for("personalReview.personalReview"))





    return render_template('levelScreen.html')

@levelScreen_bl.route('/EndGame', methods=['POST'])
def EndGame():
    
    topUser = LeaderBoard_db(
    id_max_level = id_max_level,
    username = username,
    total_words = total_words,
    total_time = total_time
    )



    from DTO.models.LeaderBoard_db import LeaderBoard_db
    level_count = LeaderBoard_db.query.count()
    if(level_count<5):    
        return render_template('createUsername.html',topUser=topUser)


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




# Người dùng chơi xong và check thấy có đạt top trả về create User
@levelScreen_bl.route('/createUsername', methods=['GET','POST'])
def CreateUsername():
    if "createUsername" in session:
        from DTO.models.LeaderBoard_db  import LeaderBoard_db
        from GUI import db
        errorUserName =""
        
        # Hiển thị bảng xếp hạng
        leader_boards = LoadLeaderBoard()
        # nếu là post thì: 
        if request.method =="POST":
            new_username = request.form.get('username')
            if(len(new_username)<=0):
                errorUserName = "Vui lòng nhập tên!"
                return  render_template('createUsername.html',leader_boards=leader_boards, errorUserName = errorUserName)
            newTopUser = session["createUsername"]
            newTopUser.username = new_username
            db.session.add(newTopUser)
            db.session.commit()
            leader_boards = LoadLeaderBoard()
        

            return render_template('leaderBoard.html', leader_boards=leader_boards)



        return render_template('createUsername.html', leader_boards=leader_boards)


    else:

        return render_template('home.html', user = current_user)
    
    




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

def LoadLeaderBoard():
    # Hiển thị bảng xếp hạng
    from DTO.models.LeaderBoard_db  import LeaderBoard_db
    from GUI import db
    leader_boards = LeaderBoard_db.query.order_by(
    LeaderBoard_db.id_max_level.desc(),
    LeaderBoard_db.total_words.desc(),
    LeaderBoard_db.total_time.desc()
    ).limit(5).all()
    return leader_boards

