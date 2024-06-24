from GUI import db
from DTO.models.Level_db  import Level_db
from DTO.models.LeaderBoard_db  import LeaderBoard_db


def SeedData():
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


def seedLeader():
    new_leader = LeaderBoard_db(id_max_level =1,username ="Mít", total_words = 2, total_time = 3)
    db.session.add(new_leader)
    db.session.commit()
    new_leader = LeaderBoard_db(id_max_level =1,username ="Dâu", total_words = 1, total_time = 1)
    db.session.add(new_leader)
    db.session.commit()
    # new_leader = LeaderBoard_db(id_max_level =12,username ="MeoMeo", total_words = 200, total_time = 1800)
    # db.session.add(new_leader)
    # db.session.commit()
    # new_leader = LeaderBoard_db(id_max_level =14,username ="Cvat", total_words = 250, total_time = 2100)
    # db.session.add(new_leader)
    # db.session.commit()
    # new_leader = LeaderBoard_db(id_max_level =14,username ="Cá", total_words = 300, total_time = 2400)
    # db.session.add(new_leader)
    # db.session.commit()
