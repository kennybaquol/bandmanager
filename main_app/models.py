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

INVENTORYCATEGORIES = (
    ('CL', 'Clothing'),
    ('MU', 'Music'),
    ('ME', 'Merchandise')
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
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})

class InventoryItem(models.Model):
    # HAVE BUY AND SELL FUNCTIONALITY
    # HAVE SORT FUNCTIONALITY
    
    # item name, item category ?, quantity remaining, size, # bought, cost, # sold, selling price, date bought, date sold (for each instance), batch #?
    # SHIRT - t-shirt, clothing,              30,       M,  50 bought, $12 each, 20,   $15 each,    6/1/22,         6/5/22, 6/6/22, etc.         1? 
    # CD - IzMyHed CD,  music,            15,      jacket,  50 bought, $7 each, 35,    $10 each,    6/20/22,       6/21/22, 7/4/22, etc.         3?         
    # STICKER - sticker,  merch,         15
    
    category = models.CharField(max_length=12, choices=INVENTORYCATEGORIES, default=INVENTORYCATEGORIES[0][0])
    name = models.CharField('Name (Required)', max_length=150)
    size = models.CharField(max_length=50, blank=True)
    currentQuantity = models.PositiveIntegerField(default=0)
    batchCost = models.DecimalField(decimal_places=2, max_digits=20, blank=True)
    sellingPrice = models.DecimalField(decimal_places=2, max_digits=20, blank=True)
    dateBought = models.DateField(blank=True, default=date.today)
    dateSold = models.DateField(blank=True, default=date.today)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'band_id': self.id})