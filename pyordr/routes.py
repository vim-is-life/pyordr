#!/usr/bin/env python3
from flask import Blueprint, Response, render_template, url_for, request
from datetime import datetime as dt
from . import models

# Blueprint config -- this here acts like our "app" had we defined it in this file
main_blueprint = Blueprint(
    "main", __name__, template_folder="templates", static_folder="static"
)
# COLUMN_NAMES = ("Name", "Added", "Desc", "State")

# tsk = models.Task(date_added=dt.now(), name="clean backyard")
# models.db.session.add(tsk)
# tsk1 = models.Task(
#     date_added=dt.now(),
#     name="rake leaves",
#     description="must rake leaves to keep it in control",
# )
# models.db.session.add_all([tsk, tsk1])
# models.db.session.commit()


def render_tasks_table():
    tasks = models.get_all_tasks()
    possible_states = models.TaskState
    return render_template(
        "partial_task-table.html",
        # column_names=COLUMN_NAMES,
        tasklist=tasks,
        valid_states=possible_states,
    )


@main_blueprint.route("/")
def index_page():
    """Render the index page which shows a view of all registered tasks."""
    tasks = models.get_all_tasks()
    possible_states = models.TaskState
    return render_template(
        "index.html",
        # column_names=COLUMN_NAMES,
        tasklist=tasks,
        valid_states=possible_states,
    )


@main_blueprint.route("/showTable")
def display_table():
    return render_tasks_table()


@main_blueprint.route("/createTask", methods=["GET", "POST"])
def create_task():
    if request.method == "POST":
        models.add_task(
            models.Task(
                name=request.form["taskName"],
                description=request.form["taskDescription"],
                date_added=dt.now(),
                state=models.TaskState.TO_BE_DONE,
            )
        )
        return render_tasks_table()
    return render_template("partial_create-task.html")


@main_blueprint.route("/toggleTaskState/<int:id>", methods=["PUT"])
def toggle_task_state(id):
    models.toggle_state(id)
    return render_tasks_table()


@main_blueprint.route("/deleteTask/<int:id>", methods=["DELETE"])
def delete_task(id):
    models.remove_task(id)
    return render_tasks_table()


@main_blueprint.route("/updateTaskInfo/<int:id>", methods=["GET", "PUT"])
def update_task_info(id):
    # we pass the id for the orm to be able to update the relevant changes, but
    # other than that the only thing we allow is changed the name and
    # description. state changes should be made from the overview or details
    # screen.
    if request.method == "PUT":
        new_task_info = models.Task(
            id=id,
            name=request.form["newName"],
            description=request.form["newDescription"],
        )
        models.update_task(id, new_task_info)
        return render_tasks_table()
    task_to_update = models.get_task(id)
    return render_template("partial_edit-task.html", task=task_to_update)


@main_blueprint.route("/taskDetail/<int:id>")
def task_detail(id):
    task = models.get_task(id)
    return render_template("partial_task-detail.html", task=task)
