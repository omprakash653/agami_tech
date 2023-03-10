from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH
# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=100)
    emp_id=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=100)
    def __str__(self):
      return self.name 

class TimeSheet(models.Model):
    reporting_manager=models.CharField(max_length=100)
    employees = models.ManyToManyField(Emp)
    
    date  = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
 

    # def __str__(self):
    #   return self.employees.name 