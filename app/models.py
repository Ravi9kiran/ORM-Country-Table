from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    
    def __str__(self):
        return self.name
    
class States(models.Model):
    name=models.ForeignKey(Country,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=100)
    capital=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Sname