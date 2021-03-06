from flask import render_template, Blueprint, request, redirect
from models.lesson import Lesson
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


lessons_blueprint = Blueprint('lessons', __name__)


@lessons_blueprint.route('/lessons/new')
def new_lesson():
    lessons = lesson_repository.select_all()
    return render_template('lessons/new.html', all_lessons = lessons)

@lessons_blueprint.route('/lessons', methods = ['POST']) #without this ['post'] request, it will be a default 'get' request
def create_lesson():
    name = request.form['name'] 
    lesson = Lesson(name)
    lesson_repository.save(lesson)
    return redirect('/lessons') 



@lessons_blueprint.route('/lessons') #change the url here to affect the link, not in the render_template
def lessons():
    lessons = lesson_repository.select_all()
    return render_template('lessons/index.html', all_lessons = lessons) #lessons/index is the homepage for lessons.


#SHOW MEMBERS BOOKED ON LESSON
@lessons_blueprint.route('/lessons/<id>')
def show(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.members(lesson)
    member_number = len(lesson_repository.members(lesson))
    return render_template("lessons/show.html", lesson=lesson, members = members, member_number = member_number)





@lessons_blueprint.route('/lessons/<id>/edit')
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    return render_template("lessons/edit.html", lesson = lesson)


    

@lessons_blueprint.route('/lessons/<id>', methods = ['POST'])
def update_lesson(id):
    name = request.form['name']
    lesson = Lesson(name, id)
    lesson_repository.update(lesson)
    return redirect('/lessons')
