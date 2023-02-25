# models.py

from datetime import datetime
from config import db, ma


class User(db.Model):
    __tablename__ = "user"  # connects class definition to the right table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    score = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # def __init__(self, user: str, score: int):
    #     self.user = user
    #     self.score = score

    def __str__(self):  # return normal format
        return f"UserData(User: {self.user}, Score: {self.score}, Created: {self.date_created})"

    def __repr__(self):  # return dict format
        return str({"user": self.user, "score": {self.score}, "created": {str(self.date_created)}})


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)
