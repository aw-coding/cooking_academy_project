import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member_1 = Member('George Richardson')

    
    def test_member_has_name(self):
        self.assertEqual('George Richardson', self.member_1.name)