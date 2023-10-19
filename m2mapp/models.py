from django.db import models

# Create your models here.

class students(models.Model):
    st_name = models.CharField(max_length=50)
    st_class = models.IntegerField()
    


class teachers(models.Model):
    teacher_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    students = models.ManyToManyField(students, related_name='teachers')





