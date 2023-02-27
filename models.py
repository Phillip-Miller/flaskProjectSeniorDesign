# models.py

from datetime import datetime
from config import db, ma

follows = db.Table('follows',
                   db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                   db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))


# https://hackmd.io/@jpshafto/H1VbmP3yOclass
class User(db.Model):
    __tablename__ = "user"  # connects class definition to the right table
    id = db.Column(db.Integer, primary_key=True)  # this autoincrements by default
    username = db.Column(db.String(32), unique=True)
    score = db.Column(db.Integer, default=0)
    followers = db.relationship(
        "User",
        secondary=follows,
        primaryjoin=(follows.c.follower_id == id),
        secondaryjoin=(follows.c.followed_id == id),
        backref=db.backref("follows", lazy="dynamic"),
        lazy="dynamic"
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

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
