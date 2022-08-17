from django.forms import ModelForm
from .models import Venue

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'state', 'city', 'email', 'phone', 'note', 'status']