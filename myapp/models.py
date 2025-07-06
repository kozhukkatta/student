from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    fees=models.IntegerField()
    def __str__(self):
	    return self.course_name


class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    sname=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    jdate=models.DateField()
    def __str__(self):
	    return self.sname
    
class Details(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    age=models.IntegerField()
    mob=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    jdate=models.DateField()
    def __str__(self):
	    return self.user

      
