from flask import render_template, Blueprint, request, redirect
from models.lesson import Lesson
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


lessons_blueprint = Blueprint('lessons', __name__)



@lessons_blueprint.route('/lessons') #change the url here to affect the link, not in the render_template
def lessons():
    lessons = lesson_repository.select_all()
    return render_template('lessons/index.html', all_lessons = lessons) #members/index is the homepage for members.

@lessons_blueprint.route('/lessons/<id>')
def show(id):
    lesson = lesson_repository.select(id)
    member = lesson_repository.member(lessons)
    return render_template("lessons/show.html", lessons=lesson, members = members)
