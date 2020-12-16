from db.run_sql import run_sql


class Booking:
    def __init__(self, member, lesson, id = None) :
        self.member = member
        self.lesson = lesson
        self.id = id     



