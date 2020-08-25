from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'venues'

urlpatterns = [
    path('', views.home, name='venues_home'),
    path('general-information/', views.general_information, name='general-information'),
    path('prewedding-preparation/', views.prewedding_prep, name='prewedding-prep'),
    path('food-and-drink/', views.food_and_drink, name='food_and_drink'),
]