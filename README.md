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
- Need to know how to template out my overview and my details page
- Need to know how to define routes and have different things be handled based on the route
- Can use simple.css

# References
- Style used to format site:
  [simple.css on GitHub](https://github.com/kevquirk/simple.css/)
- Some guides I used:
  - <https://hackersandslackers.com/your-first-flask-application/>
  - <https://hackersandslackers.com/flask-sqlalchemy-database-models/>
  - <https://hackersandslackers.com/flask-sqlalchemy-database-models/>
- Enums in python:
  <https://docs.python.org/3/howto/enum.html>
