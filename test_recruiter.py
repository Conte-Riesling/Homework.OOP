from unittest import TestCase
from employee import Recruiter

class RecruiterTest(TestCase):
    def setUp(self):
        self.name = 'Jake'
        self.salary = 5
        self.job_title = None

    def test_init(self):
        name = 'Jake'
        salary = 5
        job_title = None
        self.assertEqual(name, 'Jake')
        self.assertEqual(salary, 5)
        self.assertEqual(job_title, None)

    def test_get_work(self):
        self.get_work = 'I come to the office and start to hiring'
        self.assertEqual(self.get_work, 'I come to the office and start to hiring')