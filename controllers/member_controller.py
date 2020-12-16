from flask import render_template, Blueprint, request, redirect, Flask
from models.member import Member
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


members_blueprint = Blueprint('members', __name__)


@members_blueprint.route('/members/new')
def new_member():
    members = member_repository.select_all()
    return render_template('members/new.html', all_members = members)

@members_blueprint.route('/members', methods = ['POST']) 
def create_member():
    name = request.form['name'] 
    member = Member(name)
    member_repository.save(member)
    return redirect('/members') #returns the browser to the index route



@members_blueprint.route('/members') #change the url here to affect the link, not in the render_template
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', all_members = members) #members/index is the homepage for members.


#SHOW LESSON BOOKINGS FOR MEMBER
@members_blueprint.route('/members/<id>')
def show(id):
    member = member_repository.select(id)
    lessons = member_repository.lessons(member)
    return render_template("members/show.html", member=member, lessons = lessons)


@members_blueprint.route('/members/<id>/edit')
def edit_member(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member = member)

@members_blueprint.route('/members/<id>', methods = ['POST'])
def update_member(id):
    name = request.form['name']
    member = Member(name, id)
    member_repository.update(member)
    return redirect('/members')


