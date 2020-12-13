from db.run_sql import run_sql
from models.booking import Booking
from models.lesson import Lesson
from models.member import Member

def save(booking):
    sql = 'INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id'
    values = (booking.member.id, booking.lesson.id)
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []
    sql = 'SELECT * FROM bookings'
    results = run_sql(sql)
