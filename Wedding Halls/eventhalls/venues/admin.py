from django.contrib import admin
from .models import Image, Venue, Pricing

# Register your models here.

admin.site.register(Image)
admin.site.register(Venue)
admin.site.register(Pricing)