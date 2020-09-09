from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

@login_required
def home(request):
    return render(request, 'venue-details.html')

@login_required
def general_information(request):
    linked_venuedetail = VenueDetail.objects.filter(venue=request.user.venue).exists()
    linked_dance = DanceFloor.objects.filter(venue=request.user.venue).exists()
    if linked_venuedetail and linked_dance:
        return redirect('venues:edit-general-information')
    venue_detail_form = VenueDetailForm(request.POST or None)
    dance_floor_form = DanceFloorForm(request.POST or None)
    venue_detail_form_2 = VenueDetailForm2(request.POST or None)
    forms = [venue_detail_form, dance_floor_form, venue_detail_form_2]
    if request.method=='POST':
        if venue_detail_form.is_valid() and dance_floor_form.is_valid() and venue_detail_form_2.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'general-information.html', {'VenueDetailForm':venue_detail_form, 
    'DanceFloorForm':dance_floor_form, 'VenueDetailForm2' : venue_detail_form_2})


@login_required
def edit_general_information(request):
    linked_venuedetail = VenueDetail.objects.filter(venue=request.user.venue).exists()
    linked_dance = DanceFloor.objects.filter(venue=request.user.venue).exists()
    if not linked_dance or not linked_venuedetail:
        return redirect('venues:general-information')
    venue_detail_form = VenueDetailForm(request.POST or None, instance=request.user.venue.venuedetail)
    dance_floor_form = DanceFloorForm(request.POST or None, instance=request.user.venue.dancefloor)
    venue_detail_form_2 = VenueDetailForm2(request.POST or None, instance=request.user.venue.venuedetail)
    forms = [venue_detail_form, dance_floor_form, venue_detail_form_2]
    if request.method=='POST':
        if venue_detail_form.is_valid() and dance_floor_form.is_valid() and venue_detail_form_2.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'general-information.html', {'VenueDetailForm':venue_detail_form, 
    'DanceFloorForm':dance_floor_form, 'VenueDetailForm2' : venue_detail_form_2})

@login_required
def prewedding_prep(request):
    linked_tasting = Tasting.objects.filter(venue=request.user.venue).exists()
    linked_rehearsal = Rehearsal.objects.filter(venue=request.user.venue).exists()
    linked_arrival_setup = ArrivalSetUp.objects.filter(venue=request.user.venue).exists()
    if linked_tasting and linked_rehearsal and linked_arrival_setup:
        return redirect('venues:edit-prewedding-prep')
    tasting_form = TastingForm(request.POST or None)
    rehearsal_form = RehearsalForm(request.POST or None)
    arrival_setup_form = ArrivalSetUpForm(request.POST or None)
    forms = [tasting_form, rehearsal_form, arrival_setup_form]
    if request.method == 'POST':
        if tasting_form.is_valid() and rehearsal_form.is_valid() and arrival_setup_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'prewedding-preparation.html', {'TastingForm' : tasting_form,
    'RehearsalForm': rehearsal_form, 'ArrivalSetUpForm' : arrival_setup_form})

@login_required
def edit_prewedding_prep(request):
    linked_tasting = Tasting.objects.filter(venue=request.user.venue).exists()
    linked_rehearsal = Rehearsal.objects.filter(venue=request.user.venue).exists()
    linked_arrival_setup = ArrivalSetUp.objects.filter(venue=request.user.venue).exists()
    if not linked_tasting or not linked_rehearsal or not linked_arrival_setup:
        return redirect('venues:prewedding-prep')
    tasting_form = TastingForm(request.POST or None, instance=request.user.venue.tasting)
    rehearsal_form = RehearsalForm(request.POST or None, instance=request.user.venue.rehearsal)
    arrival_setup_form = ArrivalSetUpForm(request.POST or None, instance=request.user.venue.arrivalsetup)
    forms = [tasting_form, rehearsal_form, arrival_setup_form]
    if request.method == 'POST':
        if tasting_form.is_valid() and rehearsal_form.is_valid() and arrival_setup_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'prewedding-preparation.html', {'TastingForm' : tasting_form,
    'RehearsalForm': rehearsal_form, 'ArrivalSetUpForm' : arrival_setup_form})

@login_required
def decorations(request):
    linked_flower = Flower.objects.filter(venue=request.user.venue).exists()
    linked_decoration = Decoration.objects.filter(venue=request.user.venue).exists()
    linked_centerpiece = CenterPiece.objects.filter(venue=request.user.venue).exists()
    if linked_flower and linked_decoration and linked_centerpiece:
        return redirect('venues:edit-decorations')
    decoration_form = DecorationForm(request.POST or None)
    centerpiece_form = CenterPieceForm(request.POST or None)
    flower_form = FlowerForm(request.POST or None)
    forms = [decoration_form, centerpiece_form, flower_form]
    if request.method == 'POST':
        if decoration_form.is_valid() and centerpiece_form.is_valid() and flower_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'decorations.html', {'DecorationForm':decoration_form, 'CenterPieceForm' : centerpiece_form,
    'FlowerForm' : flower_form})

@login_required
def edit_decorations(request):
    linked_flower = Flower.objects.filter(venue=request.user.venue).exists()
    linked_decoration = Decoration.objects.filter(venue=request.user.venue).exists()
    linked_centerpiece = CenterPiece.objects.filter(venue=request.user.venue).exists()
    if not linked_flower or not linked_decoration or not linked_centerpiece:
        return redirect('venues:decorations')
    decoration_form = DecorationForm(request.POST or None, instance=request.user.venue.decoration)
    centerpiece_form = CenterPieceForm(request.POST or None, instance=request.user.venue.centerpiece)
    flower_form = FlowerForm(request.POST or None, instance=request.user.venue.flower)
    forms = [decoration_form, centerpiece_form, flower_form]
    if request.method == 'POST':
        if decoration_form.is_valid() and centerpiece_form.is_valid() and flower_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'decorations.html', {'DecorationForm':decoration_form, 'CenterPieceForm' : centerpiece_form,
    'FlowerForm' : flower_form})

@login_required
def additional_information(request):
    if AdditionalInformation.objects.filter(venue=request.user.venue).exists():
        return redirect('venues:edit-additional-information')
    additional_information = AdditionalInformationForm(request.POST or None)
    if request.method == 'POST':
        if additional_information.is_valid():
            obj = additional_information.save(commit=False)
            obj.venue = request.user.venue
            obj.save()
        return redirect('venues:venues_home')
    return render(request, 'additional-information.html', {'AdditionalInformationForm' : additional_information})

@login_required
def edit_additional_information(request):
    if not AdditionalInformation.objects.filter(venue=request.user.venue).exists():
        return redirect('venues:additional-information')
    additional_information = AdditionalInformationForm(request.POST or None, instance=request.user.venue.additionalinformation)
    if request.method == 'POST':
        if additional_information.is_valid():
            obj = additional_information.save(commit=False)
            obj.venue = request.user.venue
            obj.save()
        return redirect('venues:venues_home')
    return render(request, 'additional-information.html', {'AdditionalInformationForm' : additional_information})

@login_required
def dietary_options(request):
    if DietaryOption.objects.filter(venue=request.user.venue).exists():
        return redirect('venues:edit-dietary-option')
    dietary_option_form = DietaryOptionForm(request.POST or None)
    if request.method == 'POST':
        if dietary_option_form.is_valid():
            obj = dietary_option_form.save(commit=False)
            obj.venue = request.user.venue
            obj.save()
        return redirect('venues:venues_home')
    return render(request, 'dietary-option.html', {'DietaryOptionForm' : dietary_option_form})

@login_required
def edit_dietary_options(request):
    if not DietaryOption.objects.filter(venue=request.user.venue).exists():
        return redirect('venues:dietary-options')
    dietary_option_form = DietaryOptionForm(request.POST or None, instance=request.user.venue.dietaryoption)
    if request.method == 'POST':
        if dietary_option_form.is_valid():
            obj = dietary_option_form.save(commit=False)
            obj.venue = request.user.venue
            obj.save()
        return redirect('venues:venues_home')
    return render(request, 'dietary-option.html', {'DietaryOptionForm' : dietary_option_form})


@login_required
def venue_images(request):
    if request.method=='POST':
        venue_image_form = VenueImageForm(request.POST, request.FILES)
        if venue_image_form.is_valid():
            image = venue_image_form.save(commit=False)
            image.venue = request.user.venue
            image.save()
    venue_image_form = VenueImageForm()
    return render(request, 'venue-images.html', {'VenueImageForm' : venue_image_form})

@login_required
def delete_image(request, id):
    venue_image = VenueImage.objects.get(id=id)
    if venue_image.venue == request.user.venue:
        venue_image.delete()
    return redirect('venues:venue-images')

@login_required
def add_drink_options(request):
    drink_option_form = DrinkOptionForm(request.POST or None)
    pricing_formset = PricingFormSet(request.POST or None)
    if request.method=='POST':
        if drink_option_form.is_valid() and pricing_formset.is_valid():
            drink_option = drink_option_form.save(commit=False)
            drink_option.venue = request.user.venue
            drink_option.save()
            for form in pricing_formset:
                pricing = form.save(commit=False)
                pricing.venue = request.user.venue
                pricing.save()
                drink_option.pricing.add(pricing)
        return redirect('venues:current-drink-pricing')
    return render(request, 'drink-options.html', {'DrinkOptionForm' : drink_option_form, 'formset' : pricing_formset})

@login_required
def add_food_option(request):
    food_option_form = FoodOptionForm(request.POST or None)
    pricing_formset = PricingFormSet(request.POST or None)
    if request.method=='POST':
        if food_option_form.is_valid() and pricing_formset.is_valid():
            food_option = food_option_form.save(commit=False)
            food_option.venue = request.user.venue
            food_option.save()
            for form in pricing_formset:
                pricing = form.save(commit=False)
                pricing.venue = request.user.venue
                pricing.save()
                food_option.pricing.add(pricing)
        return redirect('venues:current-menu-pricing')
    return render(request, 'menu-options.html', {'FoodOptionForm' : food_option_form, 'formset' : pricing_formset})

@login_required
def food_and_drink(request):
    return render(request, 'food-and-drink.html')

@login_required
def show_drink_pricing(request):
    return render(request, 'current-drink-pricing.html')

@login_required
def show_food_pricing(request):
    return render(request, 'current-menu-pricing.html')

@login_required
def ceremony_and_reception(request):
    linked_indoor = IndoorOptions.objects.filter(venue=request.user.venue).exists()
    linked_outdoor = OutdoorOptions.objects.filter(venue=request.user.venue).exists()
    if linked_indoor and linked_outdoor:
        return redirect('venues:edit-ceremony-and-reception')
    indoor_options_form = IndoorOptionsForm(request.POST or None)
    outdoor_options_form = OutdoorOptionsForm(request.POST or None)
    forms = [indoor_options_form, outdoor_options_form]
    if request.method == 'POST':
        if indoor_options_form.is_valid() and outdoor_options_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'ceremony-and-reception.html', {'IndoorOptionsForm':indoor_options_form, 'OutdoorOptionsForm' : outdoor_options_form})

@login_required
def edit_ceremony_and_reception(request):
    linked_indoor = IndoorOptions.objects.filter(venue=request.user.venue).exists()
    linked_outdoor = OutdoorOptions.objects.filter(venue=request.user.venue).exists()
    if not linked_indoor or not linked_outdoor:
        return redirect('venues:ceremony-and-reception')
    indoor_options_form = IndoorOptionsForm(request.POST or None, instance=request.user.venue.indooroptions)
    outdoor_options_form = OutdoorOptionsForm(request.POST or None, instance=request.user.venue.outdooroptions)
    forms = [indoor_options_form, outdoor_options_form]
    if request.method == 'POST':
        if indoor_options_form.is_valid() and outdoor_options_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'ceremony-and-reception.html', {'IndoorOptionsForm':indoor_options_form, 'OutdoorOptionsForm' : outdoor_options_form})


@login_required
def staffing(request):
    staff_form_set = StaffFormSet(request.POST or None)
    if request.method == 'POST':
        if staff_form_set.is_valid():
            for form in staff_form_set:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'staffing-options.html', {'formset' : staff_form_set})



@login_required
def accommodations_and_parking(request):
    linked_overnight = Overnight.objects.filter(venue=request.user.venue).exists()
    linked_parking = Parking.objects.filter(venue=request.user.venue).exists()
    if linked_overnight and linked_parking:
        return redirect('venues:edit-accommodations-and-parking')
    overnight_form = OvernightForm(request.POST or None)
    parking_form = ParkingForm(request.POST or None)
    forms = [overnight_form, parking_form]
    if request.method == 'POST':
        if overnight_form.is_valid() and parking_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'accommodations-and-parking.html', {'OvernightForm' : overnight_form, 'ParkingForm' : parking_form})

@login_required
def edit_accommodations_and_parking(request):
    linked_overnight = Overnight.objects.filter(venue=request.user.venue).exists()
    linked_parking = Parking.objects.filter(venue=request.user.venue).exists()
    if not linked_overnight or not linked_parking:
        return redirect('venues:accommodations-and-parking')
    overnight_form = OvernightForm(request.POST or None, instance=request.user.venue.overnight)
    parking_form = ParkingForm(request.POST or None, instance=request.user.venue.parking)
    forms = [overnight_form, parking_form]
    if request.method == 'POST':
        if overnight_form.is_valid() and parking_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'accommodations-and-parking.html', {'OvernightForm' : overnight_form, 'ParkingForm' : parking_form})


@login_required
def payment_options(request):
    linked_payment_plan = PaymentPlan.objects.filter(venue=request.user.venue).exists()
    linked_payment_method = PaymentMethod.objects.filter(venue=request.user.venue).exists()
    if linked_payment_plan and linked_payment_method:
        return redirect('venues:edit-payment-options')
    payment_plan_form = PaymentPlanForm(request.POST or None)
    payment_method_form = PaymentMethodForm(request.POST or None)
    forms = [payment_plan_form, payment_method_form]
    if request.method == 'POST':
        if payment_plan_form.is_valid() and payment_method_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'payment-options.html', {'PaymentPlanForm' : payment_plan_form, 'PaymentMethodForm' : payment_method_form})

@login_required
def edit_payment_options(request):
    linked_payment_plan = PaymentPlan.objects.filter(venue=request.user.venue).exists()
    linked_payment_method = PaymentMethod.objects.filter(venue=request.user.venue).exists()
    if not linked_payment_plan or not linked_payment_method:
        return redirect('venues:payment-options')
    payment_plan_form = PaymentPlanForm(request.POST or None, instance=request.user.venue.paymentplan)
    payment_method_form = PaymentMethodForm(request.POST or None, instance=request.user.venue.paymentmethod)
    forms = [payment_plan_form, payment_method_form]
    if request.method == 'POST':
        if payment_plan_form.is_valid() and payment_method_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'payment-options.html', {'PaymentPlanForm' : payment_plan_form, 'PaymentMethodForm' : payment_method_form})


@login_required
def contact_info(request):
    linked_event_day_contact = EventDayContact.objects.filter(venue=request.user.venue).exists()
    linked_general_contact = GeneralContact.objects.filter(venue=request.user.venue).exists()
    if linked_event_day_contact and linked_general_contact:
        return redirect('venues:edit-contact-info')
    general_contact_form = GeneralContactForm(request.POST or None)
    event_day_contact_form = EventDayContactForm(request.POST or None)
    forms = [general_contact_form, event_day_contact_form]
    if request.method == 'POST':
        if general_contact_form.is_valid() and event_day_contact_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'contact-details.html', {'GeneralContactForm': general_contact_form, 'EventDayContactForm': event_day_contact_form})

@login_required
def edit_contact_info(request):
    linked_event_day_contact = EventDayContact.objects.filter(venue=request.user.venue).exists()
    linked_general_contact = GeneralContact.objects.filter(venue=request.user.venue).exists()
    if not linked_event_day_contact or not linked_general_contact:
        return redirect('venues:contact-info')
    general_contact_form = GeneralContactForm(request.POST or None, instance=request.user.venue.generalcontact)
    event_day_contact_form = EventDayContactForm(request.POST or None, instance=request.user.venue.eventdaycontact)
    forms = [general_contact_form, event_day_contact_form]
    if request.method == 'POST':
        if general_contact_form.is_valid() and event_day_contact_form.is_valid():
            for form in forms:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'contact-details.html', {'GeneralContactForm': general_contact_form, 'EventDayContactForm': event_day_contact_form})

@login_required
def wedding_cake(request):
    wedding_cake_form = WeddingCakeForm(request.POST or None)
    pricing_formset = PricingFormSet(request.POST or None)
    if request.method=='POST':
        if wedding_cake_form.is_valid() and pricing_formset.is_valid():
            wedding_cake = wedding_cake_form.save(commit=False)
            wedding_cake.venue = request.user.venue
            wedding_cake.save()
            for form in pricing_formset:
                pricing = form.save(commit=False)
                pricing.venue = request.user.venue
                pricing.save()
                wedding_cake.pricing.add(pricing)
            return redirect('venues:current-cake-details')
    return render(request, 'wedding-cake.html', {'WeddingCakeForm' : wedding_cake_form, 'formset' : pricing_formset})

@login_required
def show_wedding_cake(request):
    return render(request, 'current-wedding-cake-details.html')

@login_required
def photography(request):
    linked_photography = PhotoVideo.objects.filter(venue=request.user.venue).exists()
    if linked_photography:
        return redirect('venues:edit-photography')
    photography_form = PhotoVideoForm(request.POST or None)
    if request.method=='POST':
        if photography_form.is_valid():        
            obj = photography_form.save(commit=False)
            obj.venue = request.user.venue
            obj.save()
            return redirect('venues:venues_home')
    return render(request, 'photography.html', {'PhotoVideoForm' : photography_form})


@login_required
def edit_photography(request):
    linked_photography = PhotoVideo.objects.filter(venue=request.user.venue).exists()
    if not linked_photography:
        return redirect('venues:photography')
    photography_form = PhotoVideoForm(request.POST or None, instance=request.user.venue.photovideo)
    if request.method=='POST':
        if photography_form.is_valid():
            for form in photography_form:
                obj = form.save(commit=False)
                obj.venue = request.user.venue
                obj.save()
            return redirect('venues:venues_home')
    return render(request, 'photography.html', {'PhotoVideoForm' : photography_form})




