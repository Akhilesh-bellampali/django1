from django.db import models

class Student(models.Model):
    registration_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

