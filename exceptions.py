import csv
import datetime
import traceback
class EmailAlreadyExistsException(Exception):
    pass
class Employee:
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def salary_day(self, new_day):
        x = new_day
        if salary.day == salary:
            return new_day
        else:
            return new_day[0] + 1

    def get_work(self, default):
        return 'I come to the office'

    def check_salary(self, days):
        workdays = self._get_workdays()
        salary = workdays * self.salary
        return salary

    def _get_workdays(self):
        import datetime

        today = datetime.date.today()
        start_of_month = datetime.date(today.year, today.month, 1)

        workdays = 0
        current_day = start_of_month
        while current_day <= today:
            if current_day.weekday() < 5:  # з пн по пт (з 0 до 4)
                workdays += 1
            current_day += datetime.timedelta(days=1)

        return workdays

    def save_email(self):
        with open('emails.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.email])

    def validate(self):
        try:
            with open('emails.csv', 'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if self.email == row[0]:
                        raise EmailAlreadyExistsException

        except EmailAlreadyExistsException as e:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            error_message = f"{formatted_datetime} | {str(e)}\n"

            traceback_info = traceback.format_exc()
            error_message += traceback_info

            with open('logs.txt', 'a') as logfile:
                logfile.write(error_message)

class Recruiter(Employee):
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        print(recruiter.name, recruiter.salary, recruiter.job_title)

    def get_work(self, default):
        return 'I come to the office and start to hiring'

class Developer(Employee):
    def __init__(self, name, salary, job_title, tech_stack):
        self.name = name
        self.salary = salary
        self.job_title = job_title
        self.tech_stack = tech_stack
        print(developer.name, developer.salary, developer.job_title)

    def get_work(self, default):
        return 'I come to the office and start to coding'

    def __str__(self):
        return f"job_title: {self.job_title}, name: {self.name}"

    def __gt__(self, new):
        if isinstance(new, Employee):
            return self.salary > new.salary
        return False

    def __it__(self, new):
        if isinstance(new, Employee):
            return self.salary < new.salary
        return False

    def __ge__(self, new):
        if isinstance(new, Employee):
            return self.salary >= new.salary
        return False

    def __le__(self, new):
        if isinstance(new, Employee):
            return self.salary <= new.salary
        return False

    def eq(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def add(self, other):
        name = self.name + " " + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        daily_salary = max(self.daily_salary, other.daily_salary)
        return Developer(name, daily_salary, tech_stack)

ecruiter = Employee('Jake', 5, Recruiter)
print(Recruiter)
print('I come to the office and start to hiring')

Developer = Employee('Tom', 6, Developer)
print(Developer)
print('I come to the office and start to coding')


