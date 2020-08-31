from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'venues'

urlpatterns = [
    path('', views.home, name='venues_home'),
    path('general-information/', views.general_information, name='general-information'),
    path('edit-general-information/', views.edit_general_information, name='edit-general-information'),
    path('prewedding-preparation/', views.prewedding_prep, name='prewedding-prep'),
    path('edit-prewedding-preparation/', views.edit_prewedding_prep, name='edit-prewedding-prep'),
    path('food-and-drink/', views.food_and_drink, name='food-and-drink'),
    path('edit-food-and-drink/', views.edit_food_and_drink, name='edit-food-and-drink'),
    path('ceremony-and-reception/', views.ceremony_and_reception, name='ceremony-and-reception'),
    path('edit-ceremony-and-reception/', views.edit_ceremony_and_reception, name='edit-ceremony-and-reception'),
    path('staffing/', views.staffing, name='staffing'),
    path('edit-staffing/', views.edit_staffing, name='edit-staffing'),
    path('accommodations-and-parking/', views.accommodations_and_parking, name='accommodations-and-parking'),
    path('edit-accommodations-and-parking/', views.edit_accommodations_and_parking, name='edit-accommodations-and-parking'),
    path('payment-options/', views.payment_options, name='payment-options'),
    path('edit-payment-options/', views.edit_payment_options, name='edit-payment-options'),
    path('contact-info/', views.contact_info, name='contact-info'),
    path('edit-contact-info/', views.edit_contact_info, name='edit-contact-info'),
    path('decorations/', views.decorations, name='decorations'),
    path('edit-decorations/', views.edit_decorations, name='edit-decorations'),
    path('additional-information/', views.additional_information, name='additional-information'),
    path('edit-additional-information/', views.edit_additional_information, name='edit-additional-information'),
    path('venue-pictures/', views.venue_images, name='venue-images'),
    path('delete-venue-pictures/<int:id>', views.delete_image, name='delete-image')
]