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
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
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
    name = models.CharField(max_length=150)
    date = models.DateField() # ** USE https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html **
    setTime = models.CharField(max_length=150) # The time your band will be performing
    address = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    foh = models.CharField(max_length=150, blank=True) # Front of house/sound person
    fohConfirmed = models.BooleanField() # Is the sound person confirmed?
    note = models.CharField(max_length=150, blank=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.get_status_display()} on {self.name}"
        return self.name

    # class Meta:
    #     ordering = ['-status']
    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})