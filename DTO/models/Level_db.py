from GUI import db

class Level_db(db.Model):
    __tablename__ = 'Levels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phrase_count = db.Column(db.Integer, nullable=False)
    word_count = db.Column(db.Integer, nullable=False)
