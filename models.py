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
    Day      = models.ForeignKey('Day', on_delete=models.CASCADE)
    Pin      = models.PositiveIntegerField(validators=[MinValueValidator(1000),
                                       MaxValueValidator(9999)])
    Instrument = models.CharField(max_length=30, default='No Instrument Selected')

    def __str__(self):
        return self.Rollno

class Slot(models.model):
    TIME_CHOICES = (
        ('08:30 - 09:30', '08:30-09:30'),
        ('09:30 - 10:30', '09:30-10:30'),
        ('10:30 - 11:30', '10:30-11:30'),
        ('11:30 - 12:30', '11:30-12:30'),
        ('12:30 - 01:30', '12:30-01:30'),
        ('01:30 - 02:30', '01:30-02:30'),
        ('02:30 - 03:30', '02:30-03:30'),
        ('03:30 - 04:30', '03:30-04:30'),
    )

    Time = models.CharField(choices=TIME_CHOICES)

    def __str__(self):
        return self.Starttime' - 'self.Endtime

class Day(models.model):
    Slots = models.ManyToManyField(Slot)

     DAY_CHOICES = (
        ('SUN', 'Sunday'),
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
    )

    Day = models.CharField( max_length=3, choices=DAY_CHOICES )

    def __str__(self):
        return self.Day

class Cancel(models.Model):
    id = models.AutoField(primary_key=True,default=0)
    Rollno   = models.CharField(max_length=10)
    Pin      = models.PositiveIntegerField(validators=[MinValueValidator(1000),
                                       MaxValueValidator(9999)])
    def __str__(self):
        return self.Rollno
