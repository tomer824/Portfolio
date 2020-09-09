from django import forms
from .models import Customer, Venue
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = ['user', 'slug']

class CustomUserSignup(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'password2' : 'Password Confirmation',
        }


