from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from venues.filters import VenueFilter
from venues.models import Venue
from django.db.models import Q
from django.views.decorators.http import require_http_methods

# Create your views here.



@login_required
def home(request):
    filter = VenueFilter(request.GET, queryset=Venue.objects.all())
    return render(request, 'customer_welcome.html', {'filter': filter})

@login_required
@require_http_methods(['POST'])
def search_bar(request):
    if request.method=='POST':
        text=request.POST.get('customer_search_bar')
        venues = Venue.objects.filter(Q(hall_name__icontains=text) | Q(zipcode=text))
    return render(request, 'search-results.html', {'venues' : venues})

@login_required
def show_venue(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-venue-main.html', {'venue' : venue})

@login_required
def show_food(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-food.html', {'venue' : venue})

@login_required
def show_drink(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-drink.html', {'venue' : venue})

@login_required
def show_accommodations_and_parking(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-accommodations.html', {'venue' : venue})

@login_required
def show_ceremony_and_reception(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-ceremony-and-reception.html', {'venue' : venue})

@login_required
def show_decorations(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-decorations.html', {'venue' : venue})

@login_required
def show_staffing(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-staffing.html', {'venue' : venue})

@login_required
def show_payment(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-payment.html', {'venue' : venue})

@login_required
def prewedding_prep(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'prewedding-prep.html', {'venue' : venue})

@login_required
def show_contact_information(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-contact-information.html', {'venue' : venue})

@login_required
def show_additional_details(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-additional-details.html', {'venue' : venue})

@login_required
def show_photography(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-photography.html', {'venue' : venue})

@login_required
def show_wedding_cake(request, venue_slug):
    venue = Venue.objects.get(slug=venue_slug)
    return render(request, 'show-wedding-cake.html', {'venue' : venue})