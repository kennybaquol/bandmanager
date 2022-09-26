from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('bands/', views.bands_index, name='bands_index'),
    path('bands/<int:band_id>/', views.bands_detail, name='detail'),
    path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
    path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
    path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),

    path('bands/<int:band_id>/add_venue/', views.add_venue, name='add_venue'),
    path('bands/<int:band_id>/venues/', views.venues_index, name='venues_index'),
    path('bands/<int:band_id>/venues/<int:venue_id>/', views.venues_detail, name='venues_detail'),
    path('bands/<int:band_id>/venues/create/', views.venues_create, name='venues_create'),
    path('bands/<int:band_id>/venues/<int:venue_id>/update/', views.venues_update, name='venues_update'),
    path('bands/<int:band_id>/venues/<int:venue_id>/edit_venue/', views.edit_venue, name='edit_venue'),
    path('bands/<int:band_id>/venues/<int:pk>/delete/', views.VenueDelete.as_view(), name='venues_delete'),

    path('bands/<int:band_id>/add_gig/', views.add_gig, name='add_gig'),
    path('bands/<int:band_id>/gigs/', views.gigs_index, name='gigs_index'),
    path('bands/<int:band_id>/gigs/<int:gig_id>/', views.gigs_detail, name='gigs_detail'),
    path('bands/<int:band_id>/gigs/create/', views.gigs_create, name='gigs_create'),
    path('bands/<int:band_id>/gigs/<int:gig_id>/update/', views.gigs_update, name='gigs_update'),
    path('bands/<int:band_id>/gigs/<int:gig_id>/edit_gig/', views.edit_gig, name='edit_gig'),
    path('bands/<int:band_id>/gigs/<int:pk>/delete/', views.GigDelete.as_view(), name='gigs_delete'),

    path('bands/<int:band_id>/add_inventoryItem/', views.add_inventoryItem, name='add_inventoryItem'),
    path('bands/<int:band_id>/inventory/', views.inventoryItems_index, name='inventoryItems_index'),

    path('bands/<int:band_id>/inventory/create/', views.inventoryItems_create, name='inventoryItems_create'),
]