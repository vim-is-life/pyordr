#!/usr/bin/env python3
from enum import IntEnum, auto
from . import db


class TaskState(IntEnum):
    """Enum representing the state of a task to be done."""

    IN_PROGRESS = auto()
    TO_BE_DONE = auto()
    COMPLETE = auto()


class Task(db.Model):
    """Data model representing a task in the database."""

    # fmt:off
    id             = db.Column(db.Integer, primary_key=True)
    date_added     = db.Column(db.DateTime,   nullable=False)
    date_completed = db.Column(db.DateTime)
    name           = db.Column(db.String(50), nullable=False)
    description    = db.Column(db.Text)
    state          = db.Column(db.Integer,    nullable=False, default=TaskState.TO_BE_DONE)
    # fmt:on
