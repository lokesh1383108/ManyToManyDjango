from django.db import models
import datetime

# Create your models here.

class students(models.Model):
    st_name = models.CharField(max_length=50)
    st_class = models.IntegerField()
    


class teachers(models.Model):
    teacher_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    students = models.ManyToManyField(students, related_name='teachers')


class certificate(models.Model):
    student = models.ForeignKey('students', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers', on_delete=models.CASCADE)
    title = models.CharField(max_length= 100)
    issue_date = models.DateField()





