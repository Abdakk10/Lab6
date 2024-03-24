from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add any other fields for the Course model

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    # Add other fields for the Student model
    courses = models.ManyToManyField(Course, related_name='students')
