#!/usr/bin/env python3
from flask import Blueprint, Response, render_template, url_for

# Blueprint config -- this here acts like our "app" had we defined it in this file
main_blueprint = Blueprint(
    "main", __name__, template_folder="templates", static_folder="static"
)


@main_blueprint.route("/")
def index():
    return render_template("all-tasks-view.html")
