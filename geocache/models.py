# models.py
from datetime import datetime
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

follows = db.Table('follows',
                   db.Column('follower_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                   db.Column('followed_id', db.Integer, db.ForeignKey('user.id'), primary_key=True))
completed_caches = db.Table('completed_caches',
                            db.Column('cache_id', db.Integer, db.ForeignKey('cache_locations.id'), primary_key=True),
                            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                            )


# https://hackmd.io/@jpshafto/H1VbmP3yOclass
class User(db.Model):
    __tablename__ = "user"  # connects class definition to the right table
    id = db.Column(db.Integer, primary_key=True)  # this autoincrements by default
    username = db.Column(db.String(32), unique=True)
    score = db.Column(db.Integer, default=0)
    completed_caches = db.relationship('CacheLocation', secondary=completed_caches, backref="users")

    following = db.relationship(
        "User",
        secondary=follows,
        primaryjoin=(follows.c.follower_id == id),
        secondaryjoin=(follows.c.followed_id == id),
        backref=db.backref("followed_by", lazy="dynamic"),
        lazy="dynamic"
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):  # return normal format
        return f"UserData(User: {self.user}, Score: {self.score}, Created: {self.date_created})"

    def __repr__(self):  # return dict format
        return str({"user": self.user, "score": {self.score}, "created": {str(self.date_created)}})


# TIMESTAMP = LAST MODIFIED
class CacheLocation(db.Model):
    __tablename__ = "cache_locations"
    id = db.Column(db.Integer, primary_key=True)
    cachename = db.Column(db.String(64))
    longitude = db.Column(db.Float(4))
    latitude = db.Column(db.Float(4))
    hints = db.Column(db.String(256))
    trivia = db.Column(db.String(256))
    difficulty = db.Column(db.SmallInteger)
    verificationString = db.Column(db.String(20))
    radius = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f"CacheData(Cache: {self.cachename}, Difficulty: {self.difficulty}, Created: {self.timestamp})"

    def __repr__(self):
        return str({"cache": self.cachename, "difficulty": self.difficulty, "created": {str(self.timestamp)}})


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        include_relationships = True
        load_instance = True
        sqla_session = db.session


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class CacheLocationsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CacheLocation
        load_instance = True
        include_fk = True
        include_relationships = True
        sqla_session = db.session


cache_location_schema = CacheLocationsSchema()
cache_locations_schema = CacheLocationsSchema(many=True)
