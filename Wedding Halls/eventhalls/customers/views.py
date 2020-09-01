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



        