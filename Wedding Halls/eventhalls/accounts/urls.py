from django.urls import path
from . import views
from customers import views as customer_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('customer-signup/', views.customer_signup, name = 'customer-signup'),
    path('venue-signup/', views.venue_signup, name='venue-signup'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('router/', views.router, name='router'),
]