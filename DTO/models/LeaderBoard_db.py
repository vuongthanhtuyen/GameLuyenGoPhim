from GUI import db
from sqlalchemy.sql import func

class LeaderBoard_db(db.Model):
    __tablename__ = 'LeaderBoard'
    id = db.Column(db.Integer, primary_key=True)
    id_max_level = db.Column(db.Integer, db.ForeignKey('Levels.id'), nullable=False)
    record_date = db.Column(db.DateTime(timezone=True), default=func.now())
    username = db.Column(db.String(100), nullable=False)
    total_words = db.Column(db.Integer, nullable=False)
    total_time = db.Column(db.Integer, nullable=False)

    level = db.relationship('Level_db', backref=db.backref('leaderboards', lazy=True))
