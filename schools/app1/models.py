from django.db import models

class School(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    principal=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')
    def __str__(self):
        return self.name