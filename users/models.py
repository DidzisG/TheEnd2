from django.db import models


class StudentModel(models.Model):
    name = models.CharField(max_length=100, default='xx')
    grades = models.CharField(max_length=100, default='xx')

