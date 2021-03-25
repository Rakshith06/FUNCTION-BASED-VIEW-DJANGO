from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.IntegerField()
    eadd=models.CharField(max_length=50)
    
