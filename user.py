from flask import abort, make_response, jsonify
from config import db, app
from models import User, user_schema, users_schema


# @FIXME following should be null at creation
def create(body):
    username = body.get("username")
    existing_user = User.query.filter(User.username == username).one_or_none()

    if existing_user is None:
        new_user = user_schema.load(body, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(406, f"username with username {username} already exists")


def read_all():
    users = User.query.all()
    return users_schema.dump(users)


def read_one(user_id: int):
    user = User.query.filter(User.id == user_id).one_or_none()

    if user is not None:
        return user_schema.dump(user)
    else:
        abort(404, f"username with username {user_id} not found")


# should check to make sure following person actually exists -> update to patch in next iteration
def update(user_id: int, body):  # something is broken here not sure what
    existing_user = User.query.filter(User.id == user_id).one_or_none()

    if existing_user:  # @FIXME not updating every field yet @FIXME not sure if it validates bad input

        update_user = user_schema.load(body, session=db.session)
        # existing_user = user_schema.load(update_user, partial=True)

        existing_user.username = update_user.username
        existing_user.score = update_user.score

        db.session.merge(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 201
    else:
        abort(404, f"username with user_id {user_id} not found")


def delete(user_id: int):
    existing_user = User.query.filter(User.id == user_id).one_or_none()

    if existing_user:
        db.session.delete(existing_user)
        db.session.commit()
        return user_schema.dump(existing_user), 204
    else:
        abort(404, f"User with id {user_id} not found")
