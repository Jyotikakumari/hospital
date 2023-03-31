from django.db import models

# Create your models here.
class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)

    def __str__(self):
        return self.Name
    
class Patient(models.Model):
    Name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    Address = models.TextField()


    def __str__(self):
        return self.Name    
