from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=50)
    address = models.TextField()
    date_of_joining = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return self.name

class Performance(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    review_date = models.DateField()

    def __str__(self):
        return f"Review for {self.employee.name} on {self.review_date}"