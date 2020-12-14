from flask import render_template, Blueprint, request, redirect
from models.lesson import Lesson
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint('bookings', __name__)


# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)


# NEW
@bookings_blueprint.route("/bookings/new")
def new_booking():
    member = member_repository.select_all()
    lesson = lesson_repository.select_all()
    return render_template("bookings/new.html", members=members, lessons=lessons)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    lesson_id = request.form["lesson_id"]
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    new_booking = Booking(member, lesson)
    booking_repository.save(new_booking)
    return redirect("/bookings")


@bookings_blueprint.route('/bookings/<id>')
def show(id):
    booking = booking_repository.select(id)
    #lessons = member_repository.lessons(member)
    return render_template("bookings/show.html", booking = booking)