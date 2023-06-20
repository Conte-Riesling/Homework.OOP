from unittest import TestCase
from employee import Employee

class EmployeeTest(TestCase):
    def setUp(self):
        self.name = 'Jake'
        self.salary = 5
        self.job_title = None
        self.salary_day = None
        self.check_salary = None
        self.workdays = 5


    def test_init(self):
        name = 'Jake'
        salary = 5
        job_title = None
        self.assertEqual(name, 'Jake')
        self.assertEqual(salary, 5)
        self.assertEqual(job_title, None)

    def test_salary_day(self):
        self.assertEqual(self.salary_day, None)

    def test_check_salary(self):
        self.assertEqual(self.check_salary, None)


