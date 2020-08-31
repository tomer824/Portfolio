import django_filters
from accounts .models import Venue

class VenueFilter(django_filters.FilterSet):
    max_guests = django_filters.NumberFilter(field_name = 'venuedetail__max_guests', label='Guests', lookup_expr='gte')
    outdoor_ceremony = django_filters.BooleanFilter(field_name = 'outdooroptions__outdoor_ceremony', label='Outdoor Ceremony Option')
    class Meta:
        model = Venue
        fields = ['city', 'zipcode']

# dietary options