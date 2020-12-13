import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository
from models.member import Member
from models.lesson import Lesson
from models.booking import Booking


member_1 = Member('John Smith')
member_2 = Member('Jill Jones')
member_repository.save(member_1)
member_repository.save(member_2)
member_repository.select_all

lesson_1 = Lesson('Sushi Basics')
lesson_repository.save(lesson_1)

booking_1 = Booking(member_1, lesson_1)
booking_repository.save(booking_1)

