from flask import abort, make_response
from models import Cachelocations, cache_location_schema, cache_locations_schema
from config import db, app


def create(cache_locations):
    existing_cache_location = Cachelocations.query.filter(Cachelocations.cachename == cache_locations.get('cachename')).one_or_none()

    if existing_cache_location is None:
        new_cache_location = cache_location_schema.load(cache_locations, session=db.session)
        db.session.add(new_cache_location)
        db.session.commit()
        return cache_location_schema.dump(new_cache_location), 201
    else:
        abort(406, f"Cache location with name {cache_locations.get('cachename')} already exists")

def read_all():
    cache_locations = Cachelocations.query.all()
    return cache_locations_schema.dump(cache_locations)

def read_one(cache_location_id: int):
    cache_location = Cachelocations.query.filter(Cachelocations.id == cache_location_id).one_or_none()

    if cache_location is not None:
        return cache_location_schema.dump(cache_location)
    else:
        abort(404, f"Cache location with id {cache_location_id} not found")

def update(cache_location_id: int, cache_location):
    existing_cache_location = Cachelocations.query.filter(Cachelocations.id == cache_location_id).one_or_none()

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
    existing_cache_location = Cachelocations.query.filter(Cachelocations.id == cache_location_id).one_or_none()

    if existing_cache_location:
        db.session.delete(existing_cache_location)
        db.session.commit()
        return make_response(f"Cache location with id {cache_location_id} successfully deleted", 200)
    else:
        abort(404, f"Cache location with id {cache_location_id} not found")
