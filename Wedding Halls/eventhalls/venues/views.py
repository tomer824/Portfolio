from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import VenueDetailForm, DanceFloorForm, VenueDetailForm2, TastingForm, RehearsalForm, DecorationForm, CenterPieceForm, ArrivalSetUpForm, DrinkOptionForm, PricingForm, PricingFormSet
from .models import Pricing, DrinkOption

# Create your views here.

@login_required
def home(request):
    return render(request, 'venue-details.html')

@login_required
def general_information(request):
    
    venue_detail_form = VenueDetailForm(request.POST or None)
    dance_floor_form = DanceFloorForm(request.POST or None)
    venue_detail_form_2 = VenueDetailForm2(request.POST or None)
    tasting_form = TastingForm(request.POST or None)
    rehearsal_form = RehearsalForm(request.POST or None)
    decoration_form = DecorationForm(request.POST or None)
    centerpiece_form = CenterPieceForm(request.POST or None)
    arrival_setup_form = ArrivalSetUpForm(request.POST or None)

    # if keyword_form.is_valid and another_form.is_valid():
        # do whatever

    return render(request, 'general-information.html', {'VenueDetailForm':venue_detail_form, 
    'DanceFloorForm':dance_floor_form, 'VenueDetailForm2' : venue_detail_form_2})

@login_required
def prewedding_prep(request):
    tasting_form = TastingForm(request.POST or None)
    rehearsal_form = RehearsalForm(request.POST or None)
    decoration_form = DecorationForm(request.POST or None)
    centerpiece_form = CenterPieceForm(request.POST or None)
    arrival_setup_form = ArrivalSetUpForm(request.POST or None)

    return render(request, 'prewedding-preparation.html', {'TastingForm' : tasting_form,
    'RehearsalForm': rehearsal_form, 'DecorationForm':decoration_form, 'CenterPieceForm' : centerpiece_form,
    'ArrivalSetUpForm' : arrival_setup_form})

@login_required
def food_and_drink(request):
    drink_option_form = DrinkOptionForm(request.POST or None)
    formsets = []
    for prefix in ['full_open_bar','bottom_shelf', 'wine_and_beer', 'wine_only', 'beer_only']:
        formset = PricingFormSet(prefix=prefix)
        formsets.append(formset)
    form_formsets = zip(drink_option_form, formsets)
    if request.method == 'POST':
        drink_option, created = DrinkOption.objects.get_or_create(venue=request.user.venue)
        for prefix in ['full_open_bar','bottom_shelf', 'wine_and_beer', 'wine_only', 'beer_only']:
            formset = PricingFormSet(request.POST, prefix=prefix)
            if formset.is_valid():
                for form in formset:
                    pricing = form.save(commit=False)
                    pricing.venue = request.user.venue
                    pricing.save()
                    getattr(drink_option, prefix).add(pricing)
    return render(request, 'food-and-drink.html', {'form_formsets': form_formsets})

    





