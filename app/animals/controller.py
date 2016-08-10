import logging
from bson import ObjectId
from flask import Blueprint, jsonify, request, Response
from pydantic import ValidationError
import pymongo
import bson.json_util as json_util
from .model import Animal
from app.db import get_animal_collection

bp = Blueprint('animals', __name__)


@bp.route('/', methods=['POST'])
def create_animal():
    logging.info('create_animal', request.json)
    try:
        animals_collection = get_animal_collection()
        animal = Animal(**request.json)
        logging.info('Animal object', animal)
        insert = animals_collection.insert_one(dict(animal))
        return {'_id': str(insert.inserted_id)}
    except ValidationError as e:
        logging.error('Validation failed', e.errors())
        return jsonify(e.errors())
    except pymongo.errors.DuplicateKeyError as e:
        logging.error('Duplicate entry', e)
        return {'msg': 'Duplicate entry'}
    except Exception as e:
        logging.error('Uncaught error', e)
        return {'msg': 'Caught an uncaught error'}


@bp.route('/', methods=['GET'])
def get_animals():
    logging.info('fetching all animals')
    try:
        animals_collection = get_animal_collection()
        animals = animals_collection.find({})
        return Response(
            json_util.dumps(animals),
            content_type='application/json',
        )
    except Exception as e:
        logging.error('Failed to fetch animals', e)
        return {'msg': 'Failed to fetch animals'}


@bp.route('/<ObjectId:id>', methods=['GET'])
def get_animal(id):
    logging.info('fetching animal by id', id)
    try:
        animals_collection = get_animal_collection()
        animal = animals_collection.find_one(id)
        return Response(
            json_util.dumps(animal),
            content_type='application/json',
        )
    except Exception as e:
        logging.error('Failed to fetch by id', e)
        return {'msg': 'Failed to fetch by id'}


@bp.route('/<id>', methods=['PUT'])
def update_animal(id):
    logging.info('Updating animal by id')
    try:
        animals_collection = get_animal_collection()
        animal = Animal(**request.json)
        logging.info('Animal object', animal)
        response = animals_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': dict(animal)},
        )
        return {
            'matched_count': response.matched_count,
            'modified_count': response.modified_count,
        }
    except Exception as e:
        logging.error('Failed to update animal', e)
        return {'msg': 'Failed to update animal'}


@bp.route('/<ObjectId:id>', methods=['DELETE'])
def delete_animal(id):
    logging.info('Deleting animal by id', id)
    try:
        animals_collection = get_animal_collection()
        animals = animals_collection.delete_one({'_id': ObjectId(id)})
        return jsonify({'deleted_count': animals.deleted_count})
    except Exception as e:
        logging.error('Failed to delete animal', e)
        return {'msg': 'Failed to delete animal'}
