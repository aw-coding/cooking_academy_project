import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository
from models.member import Member
from models.lesson import Lesson
from models.booking import Booking
import pdb


member_1 = Member('John Smith')
member_2 = Member('Jill Jones')
member_3 = Member('Samantha Ferguson')
member_repository.save(member_1)
member_repository.save(member_2)
member_repository.save(member_3)


lesson_1 = Lesson('Sushi Basics')
lesson_2 = Lesson('German Breads: Advanced Level')
lesson_repository.save(lesson_1)
lesson_repository.save(lesson_2)

booking_1 = Booking(member_1, lesson_1)
booking_2 = Booking(member_1, lesson_2)
booking_3 = Booking(member_2, lesson_1)
booking_repository.save(booking_1)
booking_repository.save(booking_2)
booking_repository.save(booking_3)

#pdb.set_trace

# member_1.name = 'John\'s new name 443'
# member_repository.update(member_1)

