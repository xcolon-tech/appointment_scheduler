from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired')
    ]
    
    date = models.DateField()
    time = models.TimeField()
    category = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} with {self.person}"

    def save(self, *args, **kwargs):
        # Automatically set the status based on the date
        if self.date < date.today():
            self.status = 'expired'
        else:
            self.status = 'active'
        super(Appointment, self).save(*args, **kwargs)

class TimeSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
