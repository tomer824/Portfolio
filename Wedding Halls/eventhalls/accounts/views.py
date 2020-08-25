from django.shortcuts import render, redirect
from .forms import CustomerForm, VenueForm, CustomUserSignup
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def customer_signup(request):
    userform = CustomUserSignup()
    customer_form = CustomerForm()
    if request.method == 'POST':
        userform = CustomUserSignup(request.POST)
        customer_form = CustomerForm(request.POST)
        if userform.is_valid() and customer_form.is_valid():
            print('worked again')
            user = userform.save()
            customer = customer_form.save(commit = False)
            customer.user = user
            customer.save()
            return redirect('login')          
    return render(request, 'register-new-customer.html', {'userform':userform, 'customerform':customer_form})

def venue_signup(request):
    userform = CustomUserSignup()
    venue_form = VenueForm()
    if request.method == 'POST':
        userform = CustomUserSignup(request.POST)
        venue_form = VenueForm(request.POST)
        if userform.is_valid() and venue_form.is_valid():
            user = userform.save()
            venue = venue_form.save(commit = False)
            venue.user = user
            venue.save()
            return redirect('login')          
    return render(request, 'register-new-venue.html', {'userform':userform, 'venueform':venue_form})

def login(request):
    return render(request, 'login.html')

def router(request):
    try:
        if request.user.venue:
            return redirect('venues:venues_home')
    except AttributeError:
        if request.user.customer:
            return redirect('customers:home')

def logout(request):
    return render(request, 'main.html')