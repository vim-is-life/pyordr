# Work Order System
Repository for the home work order system (analogous to a todo app) that I'm making.

## Motive
As a student, I find that I'll frequently come home and my family has things that they need me to do.
The way that they tell me, however, is by verbally telling me, which at times doesn't work for me.
I work better when I see a list of things and I can check them off.
So, that's what I endeavor to do here.

## Usage
TODO

## Installation
TODO

## Goals/Nongoals
Goals:
- have a web app that lets you enter in things that need to be done
- have task entries that include
  - date added
  - date completed
  - task name
  - description
  - task state
    - either not done/done or in progress/not done/done
  - task effort parameter?
  - task time estimate?
  - task location field?
- have web frontend
  - that shows an overview page
  - that has a page that shows you the details of an item that needs to be done when you click on it
    - you can also edit the details from this page

Nongoals:
- User auth/login: I'm the only one in the house that would be doing this stuff,
  so there's not much of a use to have multiple users with different roles

## Thoughts/Ideas
- [x] Need to know how to template out my overview and my details page
- [x] Need to know how to define routes and have different things be handled based on the route
- [x] Can use simple.css
- [ ] Take out form to add new task, put it in own template, then add btn to navbar
      that will call to display the section to add a new task
- [ ] Switch out current favicon for clipboard icon that I got from icofonts

# References
- Style used to format site:
  [simple.css on GitHub](https://github.com/kevquirk/simple.css/)
- Some guides I used:
  - <https://hackersandslackers.com/your-first-flask-application/>
  - <https://hackersandslackers.com/flask-sqlalchemy-database-models/>
  - <https://hackersandslackers.com/flask-sqlalchemy-database-models/>
- Enums in python:
  <https://docs.python.org/3/howto/enum.html>
- Jinja2 templates reference:
  <https://jinja.palletsprojects.com/en/3.1.x/templates/>
- Article on using htmx with Flask:
  <https://testdriven.io/blog/flask-htmx-tailwind/#live-search-example>
- `datetime` format spec:
  <https://docs.python.org/3/library/datetime.html?highlight=strftime#strftime-and-strptime-format-codes>
- Website used to help with color scheme:
  <https://paletton.com>
- Flask-SQLAlchemy quickstart guide:
  <https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/>
- Example media queries in CSS:
  <https://www.w3schools.com/css/css3_mediaqueries_ex.asp>
- Deploying Flask app with Nginx and uWSGI:
  <https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04#step-4-configuring-uwsgi>
- One of the articles I used to decide between gunicorn and uWSGI:
  <https://medium.com/django-deployment/which-wsgi-server-should-i-use-a70548da6a83>
