from flask import abort, make_response
from geocache.models import CacheLocation, cache_location_schema, cache_locations_schema, db


def create(body):  # this was the error here
    existing_cache_location = CacheLocation.query.filter(
        CacheLocation.cachename == body.get('cachename')).one_or_none()

    if existing_cache_location is None:
        new_cache_location = cache_location_schema.load(body, session=db.session)
        db.session.add(new_cache_location)
        db.session.commit()
        return cache_location_schema.dump(new_cache_location), 201
    else:
        abort(406, f"Cache location with name {body.get('cachename')} already exists")


def read_all():
    cache_locations = CacheLocation.query.all()
    return cache_locations_schema.dump(cache_locations)


def read_one(location_id: int):
    cache_location = CacheLocation.query.filter(CacheLocation.id == location_id).one_or_none()

    if cache_location is not None:
        return cache_location_schema.dump(cache_location)
    else:
        abort(404, f"Cache location with id {location_id} not found")


def update(location_id: int, body):
    existing_cache_location = CacheLocation.query.filter(CacheLocation.id == location_id).one_or_none()
    if existing_cache_location:
        existing_cache_location = cache_location_schema.load(body, instance=existing_cache_location)
        db.session.merge(existing_cache_location)
        db.session.commit()
        return cache_location_schema.dump(existing_cache_location), 201
    else:
        abort(404, f"Cache location with id {location_id} not found")


def delete(location_id: int):
    existing_cache_location = CacheLocation.query.filter(CacheLocation.id == location_id).one_or_none()

    if existing_cache_location:
        db.session.delete(existing_cache_location)
        db.session.commit()
        # @FIXME this message is not coming across and unconvincing reply in API Return
        return cache_location_schema.dump(existing_cache_location), 204
    else:
        abort(404, f"Location with id {location_id} not found")


def verify_code(verification_string: str):
    cache_location = CacheLocation.query.filter(
        CacheLocation.verificationString == verification_string).first()

    if cache_location is not None:
        return cache_location_schema.dump(cache_location)
    else:
        abort(404, f"No cache found with matching verification string: {verification_string} not found")
