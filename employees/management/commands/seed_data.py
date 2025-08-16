import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee
from attendance.models import Attendance

class Command(BaseCommand):
    help = 'Seeds the database with fake data.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")
        fake = Faker()

        # Create departments
        departments = [Department.objects.get_or_create(name=d)[0] for d in ['HR', 'Engineering', 'Sales', 'Marketing']]

        # Create employees
        employees = []
        for _ in range(50):
            employee = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(employee)

        # Create attendance records for the past 30 days
        self.stdout.write("Creating attendance records...")
        status_choices = ['Present', 'Absent', 'Late']
        
        for employee in employees:
            # Generate attendance for past 30 days
            for days_back in range(30):
                date = datetime.now().date() - timedelta(days=days_back)
                
                # Skip if employee joined after this date
                if employee.date_of_joining > date:
                    continue
                
                # Random status with Present being more likely
                weights = [0.7, 0.2, 0.1]  # Present: 70%, Absent: 20%, Late: 10%
                status = random.choices(status_choices, weights=weights)[0]
                
                # Create attendance record
                Attendance.objects.get_or_create(
                    employee=employee,
                    date=date,
                    defaults={'status': status}
                )

        self.stdout.write(self.style.SUCCESS("Database successfully seeded with employees and attendance records!"))
