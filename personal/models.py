from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    class Meta:
        db_table = "Employee"
