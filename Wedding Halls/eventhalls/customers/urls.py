from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'customers'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_bar, name='search'),

]