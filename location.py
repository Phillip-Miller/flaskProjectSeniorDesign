from flask import abort, make_response
from models import CacheLocations, cache_location_schema, cache_locations_schema
from config import db, app


def create(location):  # this was the error here
    existing_cache_location = CacheLocations.query.filter(
        CacheLocations.cachename == location.get('cachename')).one_or_none()

    if existing_cache_location is None:
        new_cache_location = cache_location_schema.load(location, session=db.session)
        db.session.add(new_cache_location)
        db.session.commit()
        return cache_location_schema.dump(new_cache_location), 201
    else:
        abort(406, f"Cache location with name {location.get('cachename')} already exists")


def read_all():
    cache_locations = CacheLocations.query.all()
    return cache_locations_schema.dump(cache_locations)


def read_one(location_id: int):
    cache_location = CacheLocations.query.filter(CacheLocations.id == location_id).one_or_none()

    if cache_location is not None:
        return cache_location_schema.dump(cache_location)
    else:
        abort(404, f"Cache location with id {location_id} not found")


def update(cache_location_id: int, cache_location):
    existing_cache_location = CacheLocations.query.filter(CacheLocations.id == cache_location_id).one_or_none()

    if existing_cache_location:
        update_cache_location = cache_location_schema.load(cache_location, session=db.session)
        existing_cache_location.cachename = update_cache_location.cachename
        existing_cache_location.latitude = update_cache_location.latitude
        existing_cache_location.longitude = update_cache_location.longitude
        existing_cache_location.hints = update_cache_location.hints
        existing_cache_location.trivia = update_cache_location.trivia
        existing_cache_location.difficulty = update_cache_location.difficulty
        existing_cache_location.radius_accuracy = update_cache_location.radius_accuracy
        db.session.merge(existing_cache_location)
        db.session.commit()
        return cache_location_schema.dump(existing_cache_location), 201
    else:
        abort(404, f"Cache location with id {cache_location_id} not found")


def delete(cache_location_id: int):
    existing_cache_location = CacheLocations.query.filter(CacheLocations.id == cache_location_id).one_or_none()

    if existing_cache_location:
        db.session.delete(existing_cache_location)
        db.session.commit()
        return make_response(f"Cache location with id {cache_location_id} successfully deleted", 200)
    else:
        abort(404, f"Cache location with id {cache_location_id} not found")
