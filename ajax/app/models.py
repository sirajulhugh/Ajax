from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=10,null=True)
    age=models.IntegerField(null=True)
    email=models.EmailField(null=True)

