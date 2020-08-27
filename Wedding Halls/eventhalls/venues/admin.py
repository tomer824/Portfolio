from django.contrib import admin
from .models import VenueImage, Venue, Pricing

# Register your models here.

admin.site.register(VenueImage)
admin.site.register(Venue)
admin.site.register(Pricing)