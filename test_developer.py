from unittest import TestCase
from employee import Developer

class DeveloperTest(TestCase):
    def setUp(self):
        self.name = 'Tom'
        self.salary = 6
        self.job_title = None
        self.tech_stack = None

    def test_init(self):
        name = 'Tom'
        salary = 6
        job_title = None
        self.assertEqual(name, 'Tom')
        self.assertEqual(salary, 6)
        self.assertEqual(job_title, None)

    def test_get_work(self):
        self.get_work = 'I come to the office and start to coding'
        self.assertEqual(self.get_work, 'I come to the office and start to coding')

    def test_str(self):
        self.assertEqual(self.name, "Tom")
        self.assertEqual(self.job_title, None)

    def test_eq(self):
        self.assertEqual(self.tech_stack, None)



