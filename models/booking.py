# class Booking:
#     def __init__(self, id = None, member_id = None, lesson_id = None):
#         self.id = id
#         self.member_id = member_id
#         self.lesson_id =


class Booking:
    def __init__(self, member, lesson, id = None) :
        self.member = member
        self.lesson = lesson
        self.id = id        