from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from venues.filters import VenueFilter
from venues.models import Venue

# Create your views here.



@login_required
def home(request):
    filter = VenueFilter(request.GET, queryset=Venue.objects.all())
    return render(request, 'customer_welcome.html', {'filter': filter})

def search(request):
    if request.method=='POST':
        text=request.POST.get('customer_search_bar')
        