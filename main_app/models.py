from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

STATUSES = (
    ('N', 'Not Contacted'),
    ('C', 'Contacted'),
    ('F', 'Followed Up With'),
    ('B', 'Successfully Booked'),
    ('X', 'Not Going To Work')
)

class Band(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})

class Venue(models.Model):
    name = models.CharField('Name (Required)', max_length=150)
    state = models.CharField('State (Required)', max_length=150)
    city = models.CharField('City (Required)', max_length=150)
    email = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    note = models.CharField(max_length=150, blank=True)
    status = models.CharField(max_length=30, choices=STATUSES, default=STATUSES[0][0])
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.name}"

    class Meta:
        ordering = ['-status']

class Gig(models.Model):
    name = models.CharField('Name (Required)', max_length=150)
    date = models.DateField('Date (Required)') # ** USE https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html **
    state = models.CharField('State (Required)', max_length=50)
    city = models.CharField('City (Required)', max_length=50)
    address = models.CharField(max_length=150, blank=True)
    setTime = models.CharField('Set Time', max_length=50, blank=True) # The time your band will be performing
    foh = models.CharField('Sound Person', max_length=150, blank=True) # Front of house/sound person
    fohConfirmed = models.CharField('Is the sound person confirmed?', max_length=50, blank=True) # Is the sound person confirmed?
    note = models.CharField(max_length=150, blank=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.get_status_display()} on {self.name}"
        return self.name

    # class Meta:
    #     ordering = ['-status']
    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})