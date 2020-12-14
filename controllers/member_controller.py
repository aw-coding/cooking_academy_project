from flask import render_template, Blueprint, request, redirect, Flask
from models.member import Member
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository


members_blueprint = Blueprint('members', __name__)


@members_blueprint.route('/members/new')
def new_member():
    members = member_repository.select_all()
    return render_template('members/new.html', all_members = members)

@members_blueprint.route('/members', methods = ['POST']) #without this ['post'] request, it will be a default 'get' request
def create_member():
    #gather all the data from the form, 
    name = request.form['name'] #this is a dictionary, and these .form things relate to the save function in task_repository. the name value becomes a key in this dictionary
    #id    = request.form['id']       #the form this corresponds to is at the top of the tasks/new.htnl
          #form data is sent from the browser (html file) to be processed here, in the tasks_controller
    #then select a user object from the database
          #u = user_repository.select(user_id)
    # then create a new task object
    member = Member(name)
    # save the task to the database
    member_repository.save(member)
    # redirect to the INDEX
    return redirect('/members') #returns the browser to the index route



@members_blueprint.route('/members') #change the url here to affect the link, not in the render_template
def members():
    members = member_repository.select_all()
    return render_template('members/index.html', all_members = members) #members/index is the homepage for members.

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