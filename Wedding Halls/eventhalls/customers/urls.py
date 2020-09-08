from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customers'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_bar, name='search'),
    path('show/<slug:venue_slug>', views.show_venue, name='show-venue'),
    path('menu-details/<slug:venue_slug>', views.show_food, name='show-food'),
    path('drink-details/<slug:venue_slug>', views.show_drink, name='show-drink'),
    path('accommodations-and-parking/<slug:venue_slug>', views.show_accommodations_and_parking, name='show-accommodations'),
    path('ceremony-and-reception/<slug:venue_slug>', views.show_ceremony_and_reception, name='show-ceremony'),
    path('decoration-and-flower-arrangements/<slug:venue_slug>', views.show_decorations, name='show-decorations'),
    path('staffing-information/<slug:venue_slug>', views.show_staffing, name='show-staffing'),
    path('payment-information/<slug:venue_slug>', views.show_payment, name='show-payment'),
    path('prewedding-prep/<slug:venue_slug>', views.prewedding_prep, name='show-prewedding-prep'),
    path('contact-inforamtion/<slug:venue_slug>', views.show_contact_information, name='show-contact-information'),
    path('additional-details/<slug:venue_slug>', views.show_additional_details, name='show-additional-details'),
    path('photography-and-videography/<slug:venue_slug>', views.show_photography, name='show-photography'),
    path('wedding-cake/<slug:venue_slug>', views.show_wedding_cake, name='show-wedding-cake'),
]