import random
from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Department, Employee

class Command(BaseCommand):
    help = 'Seeds the database with fake data.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")
        fake = Faker()

        # Create departments
        departments = [Department.objects.get_or_create(name=d)[0] for d in ['HR', 'Engineering', 'Sales', 'Marketing']]

        # Create employees
        for _ in range(50):
            Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date='-5y', end_date='today'),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS("Database successfully seeded!"))