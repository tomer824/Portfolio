from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'venues'

urlpatterns = [
    path('', views.home, name='venues_home'),
    path('general-information/', views.general_information, name='general-information'),
    path('prewedding-preparation/', views.prewedding_prep, name='prewedding-prep'),
    path('food-and-drink/', views.food_and_drink, name='food_and_drink'),
    path('ceremony-and-reception/', views.ceremony_and_reception, name='ceremony_and_reception'),
    path('staffing/', views.staffing, name='staffing'),
    path('accommodations_and_parking/', views.accommodations_and_parking, name='accommodations_and_parking'),
    path('payment-options/', views.payment_options, name='payment-options'),
    path('contact-info/', views.contact_info, name='contact-info'),
    path('decorations/', views.decorations, name='decorations'),
    path('edit-decorations/', views.edit_decorations, name='edit-decorations'),
    path('additional-information/', views.additional_information, name='additional-information'),
    path('venue-pictures/', views.venue_images, name='venue-images')
]