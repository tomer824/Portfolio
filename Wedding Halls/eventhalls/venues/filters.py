import django_filters
from accounts .models import Venue

class VenueFilter(django_filters.FilterSet):
    max_guests = django_filters.NumberFilter(field_name = 'venuedetail__max_guests', label='Guests', lookup_expr='gte')
    outdoor_ceremony = django_filters.BooleanFilter(field_name = 'outdooroptions__outdoor_ceremony', label='Outdoor Ceremony Option')
    class Meta:
        model = Venue
        fields = ['city', 'zipcode']

class AdvanceSearch(django_filters.FilterSet):
    max_guests = django_filters.NumberFilter(field_name = 'venuedetail__max_guests', label='Guests', lookup_expr='gte')
    outdoor_ceremony = django_filters.BooleanFilter(field_name = 'outdooroptions__outdoor_ceremony', label='Outdoor Ceremony Option')
    outside_catering = django.filters.BooleanFilter(field_name= 'venuedetail__outside_catering', label='Outsided Catering Permitted')
    onsite_parking = django.filters.BooleanFilter(field_name= 'parking__onsite_parking', label='Onsite Parking Available')
    valet = django.filters.BooleanFilter(field_name= 'parking__valet', label='Valet Parking Available')
    smoking_area = django.filters.BooleanFilter(field_name= 'additional_information__designated_smoking_area', label='Designated Smoking Area')
    class Meta:
        model = Venue
        fields = ['city', 'zipcode']