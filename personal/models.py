from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Reserve(models.Model):
    id       = models.AutoField(primary_key=True)
    Rollno   = models.CharField(max_length=10)
    First    = models.CharField(max_length=25)
    Last     = models.CharField(max_length=25)
    Email    = models.EmailField(max_length=30)
    Phone    = models.CharField(max_length=15)
    Date     = models.DateField()
    Fromtime = models.TimeField()
    Totime   = models.TimeField()
    Pin      = models.PositiveIntegerField(validators=[MinValueValidator(1000),
                                       MaxValueValidator(9999)])
    Instrument = models.CharField(max_length=30, default='No Instrument Selected')

    def __str__(self):
        return self.Rollno

class Item(models.Model):
    Rollno   = models.CharField(max_length=10)
    Instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.pk

class Cancel(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    Rollno   = models.CharField(max_length=10)
    Pin      = models.PositiveIntegerField(validators=[MinValueValidator(1000),
                                       MaxValueValidator(9999)])
    def __str__(self):
        return self.Rollno
