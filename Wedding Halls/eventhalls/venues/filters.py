import django_filters
from accounts .models import Venue

class VenueFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Venue
        fields = ['max_guests']
