from django.db import models

class Users(models.Model):
    Username = models.CharField(max_length=100,unique=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Balance = models.IntegerField(default=0)
    def __str__(self):
        return self.Name
