#!/usr/bin/env python3
from enum import IntEnum, auto
from . import db


class TaskState(IntEnum):
    """Enum representing the state of a task to be done."""

    IN_PROGRESS = auto()
    TO_BE_DONE = auto()
    COMPLETE = auto()

    def __str__(self):
        if self.value == self.IN_PROGRESS:
            ret_value = "In Progress"
        if self.value == self.TO_BE_DONE:
            ret_value = "To Be Done"
        if self.value == self.COMPLETE:
            ret_value = "Complete"
        return ret_value


class Task(db.Model):
    """Data model representing a task in the database."""

    # fmt:off
    id             = db.Column(db.Integer, primary_key=True)
    date_added     = db.Column(db.DateTime,        nullable=False)
    date_completed = db.Column(db.DateTime)
    name           = db.Column(db.String(50),      nullable=False, unique=True)
    description    = db.Column(db.Text)
    state          = db.Column(db.Enum(TaskState), nullable=False, default=TaskState.TO_BE_DONE)
    # fmt:on


def get_all_tasks():
    """Return a list of all the tasks in the database."""
    stmt = db.select(Task).order_by(Task.state)
    res = db.session.execute(stmt)
    # done this way because seems to be error with returning scalars of result
    # when result contains only one row
    try:
        return res.scalars()
    except:
        return [res.scalar()]


def get_task(task_id: int):
    """Return a single task object from the database whose ID matches `task_id`"""
    return db.get_or_404(Task, task_id)


def add_task(task_to_add: Task):
    db.session.add(task_to_add)
    db.session.commit()


def toggle_state(task_id: int):
    task_to_update = db.get_or_404(Task, task_id)
    old_status = task_to_update.state
    new_status = TaskState(old_status)
    try:
        new_status = TaskState(new_status - 1)
    except:
        new_status = TaskState(3)
    task_to_update.state = new_status
    db.session.commit()


def remove_task(task_id: int):
    task = db.get_or_404(Task, task_id)
    db.session.delete(task)
    db.session.commit()


def update_task(task_id: int, new_task_info: Task):
    task_to_update = db.get_or_404(Task, task_id)
    task_to_update.name = new_task_info.name
    task_to_update.description = new_task_info.description
    db.session.commit()
