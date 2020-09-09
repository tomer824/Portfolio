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
    path('drink-options/', views.add_drink_options, name='drink-options'),
    path('dietary-option/', views.dietary_options, name='dietary-option'),
    path('menu-options/', views.add_food_option, name='food-option'),
    path('current-menu-pricing/', views.show_food_pricing, name='current-menu-pricing'),
    path('edit-dietary-option/', views.edit_dietary_options, name='edit-dietary-option'),
    path('ceremony-and-reception/', views.ceremony_and_reception, name='ceremony-and-reception'),
    path('edit-ceremony-and-reception/', views.edit_ceremony_and_reception, name='edit-ceremony-and-reception'),
    path('staffing/', views.staffing, name='staffing'),
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
    path('delete-venue-pictures/<int:id>', views.delete_image, name='delete-image'),
    path('current-drink-pricing/', views.show_drink_pricing, name='current-drink-pricing'),
    path('wedding-cake/', views.wedding_cake, name='wedding-cake'),
    path('photography-and-videography/', views.photography, name='photography'),
    path('edit-photography-and-videography/', views.edit_photography, name='edit-photography')
]

