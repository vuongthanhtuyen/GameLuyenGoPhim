from flask import Blueprint,request, render_template, flash, url_for,redirect, session, jsonify,request
from GUI import db
from datetime import date
from flask_login import current_user




levelScreen_bl = Blueprint('levelScreen', __name__,template_folder='../GUI/templates/')


# EndGamePost (id , total_time, total_word), ClearLevelPost(id)
# level = 1, số từ = 4
# --> Hiển thị 4 chữ , chơi xong 4 chữ --> gửi level về cho html --> thi hành action <Post -ClearLevelPost>  --> từ html nhận lại level 2




@levelScreen_bl.route('/Game', methods=['GET'])
def LevelScreenGet(): # Khi người dùng bấm bắt đầu
    dataSend = {'id': 1, 'word_count': 4}
    # return redirect(url_for('levelScreen', idLevel=1, word_count=4))

    return render_template('levelScreen.html', dataSend = dataSend, idLevel = 1, word_count = 4)



@levelScreen_bl.route('/Game', methods=['POST'])
def ClearLevelPost(): # level ở đây là cái lấy từ url truyền tới
    from DTO.models.Level_db import Level_db

    idLevel = int(request.form.get('idPost'))
    level = Level_db.query.filter_by(id=idLevel).first()
    if level:

        return render_template('clearLevel.html',idLevel =level.id, word_count = level.word_count)

    else:
        flash('Lỗi không thể truy vấn dữ liệu level.', category='error')
        return render_template('home.html', user = current_user)

@levelScreen_bl.route('/levelScreen', methods=['POST'])
def EndGamePost():
    
    # Thêm vào personal review khi khi người dùng endgame
    data_from_python = {'id': 2, 'recordWord': 800}
    newIdMaxLevel = int(request.form.get('id_max_level'))
    newTotalTime = float(request.form.get('total_time'))
    newTotalWord = int(request.form.get('total_words'))

    # return render_template('index.html', data_from_python=data_from_python)

    from DTO.models.LeaderBoard_db import LeaderBoard_db
    level_count = LeaderBoard_db.query.count()
    topUser = {
        "id_max_level": newIdMaxLevel,
        "username": "",
        "total_words": newTotalWord,
        "total_time": newTotalTime
    }
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
        if (topUser["id_max_level"] > lowest_leaderboard.id_max_level) or (
                (topUser["id_max_level"] == lowest_leaderboard.id_max_level) and (topUser["total_words"] > lowest_leaderboard.total_words)) or (
                (topUser["id_max_level"] == lowest_leaderboard.id_max_level) and (topUser["total_words"] == lowest_leaderboard.total_words) and (
                topUser["total_time"] > lowest_leaderboard.total_time)):
            # nếu user đạt top thì add vào một user mới
            return redirect(url_for("levelScreen.CreateUsername"))
    session.pop("createUsername",None)


    return render_template('personalReview.html',data_from_python=data_from_python)



# Người dùng chơi xong và check thấy có đạt top thì yêu cậu user nhập user name
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
            newTopUser = session.pop("createUsername")
            topUser = LeaderBoard_db(
                id_max_level=newTopUser["id_max_level"],
                username=new_username,
                total_words=newTopUser["total_words"],
                total_time=newTopUser["total_time"]
            )

            db.session.add(topUser)
            db.session.commit()
            leader_boards = LoadLeaderBoard()
        

            return render_template('leaderBoard.html', leader_boards=leader_boards)



        return render_template('createUsername.html', leader_boards=leader_boards)


    else:

        return render_template('home.html', user = current_user)
    


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


def to_dict(model):
    # """Convert SQLAlchemy model instance into a dictionary."""
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}
