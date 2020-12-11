import unittest
from models.lesson import Lesson

class TestLesson(unittest.TestCase):
    def setUp(self):
        self.lesson_1 = Lesson('Sushi Basics')

    
    def test_lesson_has_name(self):
        self.assertEqual('Sushi Basics', self.lesson_1.name)