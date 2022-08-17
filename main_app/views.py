from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Band, Venue
from .forms import VenueForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bands_index(request):
    bands = Band.objects.filter(user=request.user)
    return render(request, 'bands/index.html', { 'bands': bands })

@login_required
def venues_index(request, band_id):
  band = Band.objects.get(id=band_id)
  venues = band.venue_set.all()
  # venue_form = VenueForm()
  return render(request, 'venues/index.html', {
    'venues': venues,
    'band': band,
    # 'venue_form': venue_form
  })

@login_required
def bands_detail(request, band_id):
  band = Band.objects.get(id=band_id)
  return render(request, 'bands/detail.html', { 
    'band': band,
  })

@login_required
def venues_detail(request, band_id, venue_id):
  band = Band.objects.get(id=band_id)
  venue = Venue.objects.get(id=venue_id)
  return render(request, 'venues/detail.html', { 
    'band': band,
    'venue': venue 
  })

# GET route that takes the user to the page with the add venue form
@login_required
def venues_create(request, band_id):
  band = Band.objects.get(id=band_id)
  venue_form = VenueForm()
  return render(request, 'venues/create.html', {
    'band': band,
    'venue_form': venue_form
  })

# POST route that creates a Venue using the completed form data
@login_required
def add_venue(request, band_id):
  # create a ModelForm instance using the data in request.POST
  form = VenueForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the band_id assigned
    new_venue = form.save(commit=False)
    new_venue.band_id = band_id
    new_venue.save()
  return redirect('detail', band_id=band_id)

# GET route that takes the user to the page with the edit venue form
@login_required
def venues_update(request, band_id, venue_id):
  band = Band.objects.get(id=band_id)
  venue = Venue.objects.get(id=venue_id)
  return render(request, 'venues/update.html', {
    'band': band,
    'venue': venue
  })

# POST route that edits the current Venue using the completed form data
@login_required
def edit_venue(request, band_id, venue_id):
  # venue = Venue.objects.get(id=venue_id)
  form = VenueForm(request.POST)
  # validate the form
  if form.is_valid():
    venue = form.save(commit=False)
    band = Band.objects.get(id=band_id)
    venue.id = venue_id
    venue.band_id = band.id
    venue.save()
  return redirect('detail', band_id=band_id)

class BandCreate(LoginRequiredMixin, CreateView):
  model = Band
  fields = ['name']
  success_url = '/bands/'

  # This inherited method is called when a
  # valid band form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the band
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class VenueDelete(LoginRequiredMixin, DeleteView):
  model = Venue
  success_url = '/bands/'

# **NEED TO REMOVE ABILITY TO UPDATE AND DELETE BANDS LATER**
class BandUpdate(LoginRequiredMixin, UpdateView):
  model = Band
  fields = []

class BandDelete(LoginRequiredMixin, DeleteView):
  model = Band
  success_url = '/bands/'
# **NEED TO REMOVE ABILITY TO UPDATE AND DELETE BANDS LATER**