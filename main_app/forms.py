from django.forms import ModelForm
from .models import Venue, Gig

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'state', 'city', 'email', 'phone', 'note', 'status']

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['name', 'date', 'setTime', 'address', 'state', 'city', 'foh', 'fohConfirmed', 'note']
