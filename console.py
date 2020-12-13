import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
from models.member import Member
from models.lesson import Lesson


member_1 = Member('John Smith')
member_repository.save(member_1)

lesson_1 = Lesson('Sushi Basics')
lesson_repository.save(lesson_1)