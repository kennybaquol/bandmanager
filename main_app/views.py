from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

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

#
# INDEX VIEWS
#

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
def gigs_index(request, band_id):
  band = Band.objects.get(id=band_id)
  gigs = band.gig_set.all()
  return render(request, 'gigs/index.html', {
    'gigs': gigs,
    'band': band,
  })

@login_required
def inventoryItems_index(request, band_id):
  band = Band.objects.get(id=band_id)
  inventoryItems = band.gig_set.all()
  return render(request, 'inventoryItems/index.html', {
    'inventoryItems': inventoryItems,
    'band': band,
  })

#
# DETAIL VIEWS
#

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

@login_required
def gigs_detail(request, band_id, gig_id):
  band = Band.objects.get(id=band_id)
  gig = Gig.objects.get(id=gig_id)
  return render(request, 'gigs/detail.html', { 
    'band': band,
    'gig': gig
  })

#
# CREATE VIEWS
#

# GET route that takes the user to the page with the add venue form
@login_required
def venues_create(request, band_id):
  band = Band.objects.get(id=band_id)
  venue_form = VenueForm()
  return render(request, 'venues/create.html', {
    'band': band,
    'venue_form': venue_form
  })

# GET route that takes the user to the page with the add gig form
@login_required
def gigs_create(request, band_id):
  band = Band.objects.get(id=band_id)
  gig_form = GigForm()
  return render(request, 'gigs/create.html', {
    'band': band,
    'gig_form': gig_form
  })

# GET route that takes the user to the page with the add inventoryItem form
@login_required
def inventoryItems_create(request, band_id):
  band = Band.objects.get(id=band_id)
  inventoryItem_form = InventoryItemForm()
  return render(request, 'inventoryItems/create.html', {
    'band': band,
    'inventoryItem_form': inventoryItem_form
  })

#
# ADD VIEWS
#

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
  return redirect('venues_index', band_id=band_id)

# POST route that creates a Gig using the completed form data
@login_required
def add_gig(request, band_id):
  # create a ModelForm instance using the data in request.POST
  form = GigForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the band_id assigned
    new_gig = form.save(commit=False)
    new_gig.band_id = band_id
    new_gig.save()
  return redirect('gigs_index', band_id=band_id)

# POST route that creates an InventoryItem using the completed form data
@login_required
def add_inventoryItem(request, band_id):
  # create a ModelForm instance using the data in request.POST
  form = InventoryItemForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the band_id assigned
    new_inventoryItem = form.save(commit=False)
    new_inventoryItem.band_id = band_id
    new_inventoryItem.save()
  return redirect('inventoryItems_index', band_id=band_id)

#
# UPDATE VIEWS
#

# GET route that takes the user to the page with the edit venue form
@login_required
def venues_update(request, band_id, venue_id):
  band = Band.objects.get(id=band_id)
  venue = Venue.objects.get(id=venue_id)
  return render(request, 'venues/update.html', {
    'band': band,
    'venue': venue
  })

# GET route that takes the user to the page with the edit gig form
@login_required
def gigs_update(request, band_id, gig_id):
  band = Band.objects.get(id=band_id)
  gig = Gig.objects.get(id=gig_id)
  return render(request, 'gigs/update.html', {
    'band': band,
    'gig': gig
  })

#
# EDIT VIEWS
#

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
  return redirect('venues_index', band_id=band_id)

# POST route that edits the current Gig using the completed form data
@login_required
def edit_gig(request, band_id, gig_id):
  form = GigForm(request.POST)
  if form.is_valid():
    gig = form.save(commit=False)
    band = Band.objects.get(id=band_id)
    gig.id = gig_id
    gig.band_id = band.id
    gig.save()
  return redirect('gigs_index', band_id=band_id)

#
# GENERIC VIEWS
#

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

# **NEED TO REMOVE ABILITY TO UPDATE AND DELETE BANDS LATER**
class BandUpdate(LoginRequiredMixin, UpdateView):
  model = Band
  fields = []

class BandDelete(LoginRequiredMixin, DeleteView):
  model = Band
  success_url = '/bands/'
# **NEED TO REMOVE ABILITY TO UPDATE AND DELETE BANDS LATER**

class VenueDelete(LoginRequiredMixin, DeleteView):
  model = Venue
  success_url = '/bands/'

class GigDelete(LoginRequiredMixin, DeleteView):
  model = Gig
  success_url = '/bands/'