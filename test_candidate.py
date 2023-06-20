from unittest import TestCase
from candidate import Candidate

class CandidateTest(TestCase):
    def setUp(self):
        self.first_name = 'Jake'
        self.last_name = 'Jobson'
        self.email = 'dsa@mail.com'
        self.tech_stek = 'Phyton'
        self.main_skill = 'Django'
        self.main_skill_grade = 'Django_grade'

    def test_init(self):
        first_name = 'Jake'
        last_name = 'Jobson'
        email = 'dsa@mail.com'
        tech_stek = 'Phyton'
        main_skill = 'Django'
        main_skill_grade = 'Django_grade'
        self.assertEqual(self.first_name, 'Jake')
        self.assertEqual(self.last_name, 'Jobson')
        self.assertEqual(self.email, 'dsa@mail.com')
        self.assertEqual(self.tech_stek, 'Phyton')
        self.assertEqual(self.main_skill, 'Django')
        self.assertEqual(self.main_skill_grade, 'Django_grade')

    def test_full_name(self):
        first_name = 'Jake'
        last_name = 'Jobson'
        self.assertEqual([self.first_name, self.last_name], ['Jake', 'Jobson'])

    