# encoding: utf-8
import datetime
import peewee
from .app import db


class Todo(db.Model):
    title = peewee.CharField()
    description = peewee.TextField()
    created_at = peewee.DateTimeField(default=datetime.datetime.utcnow)
    done = peewee.BooleanField(default=False)
