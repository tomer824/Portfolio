from django.db import models
from accounts.models import Venue

# Create your models here.
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

class VenueDetail(models.Model):
    max_guests = models.IntegerField()
    min_guests = models.IntegerField(null=True, blank=True)
    recommended_tip = models.IntegerField(null=True, blank=True)
    min_fee = models.IntegerField()
    outside_catering = models.BooleanField(choices=BOOL_CHOICES)
    venue_only_price = models.IntegerField(blank=True, null = True)
    deposit_fee = models.IntegerField(null=True, blank=True)
    non_refundable_percent = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE, related_name='venuedetail')

class Kosher(models.Model):
    glatt = models.BooleanField(choices=BOOL_CHOICES)
    beit_yoseph = models.BooleanField(choices=BOOL_CHOICES)
    chalav_yisrael = models.BooleanField(choices=BOOL_CHOICES)
    kemach_yisrael = models.BooleanField(choices=BOOL_CHOICES)
    rabbinical_supervision = models.CharField(max_length=150, choices=BOOL_CHOICES)
    dietary = models.OneToOneField('DietaryOption', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class JewishWedding(models.Model):
    seperate_seating_option = models.BooleanField(choices=BOOL_CHOICES)
    seperate_dancing_option = models.BooleanField(choices=BOOL_CHOICES)
    ichud_room = models.BooleanField(choices=BOOL_CHOICES)
    bride_reception_room = models.BooleanField(choices=BOOL_CHOICES)
    groom_ketubah_room = models.BooleanField(choices=BOOL_CHOICES)
    jewish = models.OneToOneField(Kosher, on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class SeaFood(models.Model):
    lobster = models.BooleanField()
    crab = models.BooleanField()
    shrimp = models.BooleanField()
    oysters = models.BooleanField()
    sea_food_package = models.BooleanField()
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class DietaryOption(models.Model):
    vegitarian = models.BooleanField(choices=BOOL_CHOICES)
    vegan = models.BooleanField(choices=BOOL_CHOICES)
    gluten_free = models.BooleanField(choices=BOOL_CHOICES)
    lactose_free = models.BooleanField(choices=BOOL_CHOICES)
    halal = models.BooleanField(choices=BOOL_CHOICES)
    kosheroption = models.BooleanField(choices=BOOL_CHOICES)
    sea_food = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class FoodOption(models.Model):
    MEAL_CHOICES = ((True, 'Sit Down'), (False, 'Buffet'))
    meal_option = models.BooleanField(choices=MEAL_CHOICES)
    name_of_food = models.CharField(max_length=50)
    description_of_food = models.CharField(max_length=250)
    pricing = models.ManyToManyField('Pricing')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    
class DrinkOption(models.Model):
    DRINK_CHOICES = (('full_open_bar','Full Open Bar'), ('bottom_shelf', 'Bottom Shelf Only'),
    ('wine_and_beer','Wine and Beer'), ('wine_only','Wine Only'), ('beer_only','Beer Only'))
    drink_options = models.CharField(max_length=30, choices=DRINK_CHOICES,)
    pricing = models.ManyToManyField('Pricing')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

class WeddingCake(models.Model):
    CAKE_CHOICES = (('two_layer','Two Layer Cake'), ('three_layer','Three Layer Cake'), ('four_layer','Four Layer Cake'),('five_layer','Five Layer Cake'))
    cake_option = models.CharField(max_length=50, choices=CAKE_CHOICES,)
    pricing = models.ManyToManyField('Pricing')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='cakes')

class Tasting(models.Model):
    tastings_offered = models.BooleanField(choices=BOOL_CHOICES)
    tasting_price = models.IntegerField(null=True, blank=True)
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class CuttingTheCakeFee(models.Model):
    cake_cutting_fee = models.BooleanField(choices=BOOL_CHOICES)
    fee = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    
class CorkFee(models.Model):
    corkage_fee = models.BooleanField(choices=BOOL_CHOICES)
    fee = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class ClosedBottleFee(models.Model):
    closed_bottle_fee = models.BooleanField(choices=BOOL_CHOICES)
    fee = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Staff(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    number_of_guests = models.IntegerField()
    number_of_waiters = models.IntegerField()
    number_of_bartenders = models.IntegerField()
    number_of_other_staff = models.IntegerField()

class CenterPiece(models.Model):
    provide_centerpieces = models.BooleanField(choices=BOOL_CHOICES)
    basic_pricing = models.IntegerField(null=True, blank=True)
    custom_design = models.BooleanField(choices=BOOL_CHOICES)
    custom_pricing = models.IntegerField(null=True, blank=True)
    outside_centerpieces_allowed = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class DanceFloor(models.Model):
    max_capacity = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PaymentMethod(models.Model):
    accept_check = models.BooleanField(choices=BOOL_CHOICES)
    accept_credit_card = models.BooleanField(choices=BOOL_CHOICES)
    wire_transfer = models.BooleanField(choices=BOOL_CHOICES)
    cash_only = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PaymentPlan(models.Model):
    payment_plan_option = models.BooleanField(choices=BOOL_CHOICES, null=True, blank=True)
    months = models.IntegerField(null=True, blank=True)
    last_payment_deadline = models.CharField(max_length=50, null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class IndoorOptions(models.Model):
    indoor_reception = models.BooleanField(choices=BOOL_CHOICES)
    indoor_ceremony = models.BooleanField(choices=BOOL_CHOICES)
    indoor_dancing = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE, related_name='indooroptions')

class OutdoorOptions(models.Model):
    outdoor_reception = models.BooleanField(choices=BOOL_CHOICES)
    outdoor_ceremony = models.BooleanField(choices=BOOL_CHOICES)
    outdoor_dancing = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE, related_name='outdooroptions')

class RainBackUp(models.Model):
    tents_or_canopies = models.BooleanField(choices=BOOL_CHOICES)
    electric_generator = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Overnight(models.Model):
    hotel_partners = models.CharField(max_length=200, null=True, blank=True)
    room_costs = models.IntegerField(null=True, blank=True)
    bulk_rooms_discount = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Parking(models.Model):
    onsite_parking = models.BooleanField(choices=BOOL_CHOICES)
    car_max = models.IntegerField(null=True, blank=True)
    valet = models.BooleanField(choices=BOOL_CHOICES)
    valet_cost = models.IntegerField(null=True, blank=True)
    parking_cost = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Rehearsal(models.Model):
    rehearsal_ceremonies = models.BooleanField(choices=BOOL_CHOICES)
    rehearsal_dinners = models.BooleanField(choices=BOOL_CHOICES)
    rehearsal_ceremony_cost = models.IntegerField(null=True, blank=True)
    rehearsal_ceremony_pricing = models.ManyToManyField('Pricing', null=True, blank=True, related_name='rehearsal_ceremony_pricing')
    rehearsal_dinner_cost = models.IntegerField(null=True, blank=True)
    rehearsal_dinner_pricing = models.ManyToManyField('Pricing', related_name='rehearsal_dinner_pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class InsuranceAndRefund(models.Model):
    cancellation_insurance = models.BooleanField(choices=BOOL_CHOICES)
    insurance_partners = models.CharField(max_length=250, null=True, blank=True)
    cancellation_insurance_cost = models.IntegerField(null=True, blank=True)
    cancellation_policy_days = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PhotoVideo(models.Model):
    inhouse_photographer = models.BooleanField(choices=BOOL_CHOICES)
    inhouse_videographer = models.BooleanField(choices=BOOL_CHOICES)
    outside_photography = models.BooleanField(choices=BOOL_CHOICES)
    outside_videography = models.BooleanField(choices=BOOL_CHOICES)
    inhouse_photography_cost = models.IntegerField(null=True, blank=True)
    inhouse_video_cost = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Flower(models.Model):
    outside_florist = models.BooleanField(choices=BOOL_CHOICES)
    custom_floral_design = models.BooleanField(choices=BOOL_CHOICES)
    custom_floral_pricing = models.IntegerField(null=True, blank=True)
    basic_florist_pricing = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Decoration(models.Model):
    provide_decorations = models.BooleanField(choices=BOOL_CHOICES)
    decorations_pricing = models.IntegerField(null=True, blank=True)
    outside_decorations = models.BooleanField(choices=BOOL_CHOICES)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class ArrivalSetUp(models.Model):
    hours_preevent_setup = models.IntegerField(null=True, blank=True)
    hours_preevent_arrival = models.IntegerField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class EventDayContact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class GeneralContact(models.Model):
    contact_person = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class VenueImage(models.Model):
    image = models.ImageField(upload_to='venue-images/', null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

class AdditionalInformation(models.Model):
    provide_wedding_cake = models.BooleanField(choices=BOOL_CHOICES)
    candles = models.BooleanField(choices=BOOL_CHOICES)
    sparklers = models.BooleanField(choices=BOOL_CHOICES)
    indoor_smoking = models.BooleanField(choices=BOOL_CHOICES)
    designated_smoking_area = models.BooleanField(choices=BOOL_CHOICES)
    secure_room = models.BooleanField(choices=BOOL_CHOICES)
    people_per_table = models.IntegerField(null=True, blank=True)
    provide_booster_seats = models.BooleanField(choices=BOOL_CHOICES)
    provide_place_cards = models.BooleanField(choices=BOOL_CHOICES)
    ceremony_reception_seperate_rooms = models.BooleanField(choices=BOOL_CHOICES)
    ceremony_seating_provided = models.BooleanField(choices=BOOL_CHOICES)
    tip_included = models.BooleanField(choices=BOOL_CHOICES, null=True, blank=True)
    coat_room = models.BooleanField(choices=BOOL_CHOICES)
    wheelchair_accessible = models.BooleanField(choices=BOOL_CHOICES)
    other_notes = models.TextField(null=True, blank=True)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Pricing(models.Model):
    amount_of_people = models.IntegerField()
    cost = models.IntegerField()
    flat_fee = models.IntegerField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount_of_people} people for {self.cost} Dollars"
