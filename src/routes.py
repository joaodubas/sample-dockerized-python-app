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
    tasks = Todo.select()
    return jsonify({'tasks': tasks})


@app.route('todo/v1/tasks/<int:pk>', methods=('GET',))
def task(pk):
    task = Todo.select().where(id=pk)
    return jsonify({'task': task})


@app.route('todo/v1/tasks', methods=('POST',))
def create():
    task = Todo.insert()
    return jsonify({'task': task}), 201


@app.route('todo/v1/tasks/<int:pk>', methods=('PUT',))
def update(pk):
    task = Todo.update().where(id=pk)
    return jsonify({'task': task})


@app.route('todo/v1/tasks/<int:pk>', methods=('DELETE',))
def delete(pk):
    task = Todo.delete().where(id=pk)
    return jsonify({'task': None})
