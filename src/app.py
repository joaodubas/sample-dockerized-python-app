# encoding: utf-8
from flask import Flask
from flask_peewee.db import Database

app = Flask('todo-list')
app.config.from_object('confs.Configuration')
db = Database(app)


def create_tables():
    """create_tables -- Invoke the `create_table` method on all models."""
    from .models import Todo
    Todo.create_table()
