from flask import render_template, Blueprint, request, redirect
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

bookings_blueprint = Blueprint('bookings', __name__)


# @members_blueprint.route('/members') #change the url here to affect the link, not in the render_template
# def members():
#     members = member_repository.select_all()
#     return render_template('members/index.html', all_members = members) #members/index is the homepage for members.

# @members_blueprint.route('/members/<id>')
# def show(id):
#     member = member_repository.select(id)
#     lessons = member_repository.lessons(member)
#     return render_template("members/show.html", memberr=member, lessons = lessons)