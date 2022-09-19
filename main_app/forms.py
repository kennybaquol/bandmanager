from django.forms import ModelForm
from django import forms
from .models import Venue, Gig

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'state', 'city', 'email', 'phone', 'note', 'status']

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['name', 'date', 'state', 'city', 'address', 'setTime', 'foh', 'fohConfirmed', 'note']

        widgets = {
            'date' : DatePickerInput()
        }
