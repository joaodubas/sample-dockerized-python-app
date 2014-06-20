# encoding: utf-8
from flask import jsonify, abort, request, make_response, url_for
from .app import app


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('todo/v1/tasks', methods=('GET',))
def tasks():
    return jsonify({'tasks': None})
