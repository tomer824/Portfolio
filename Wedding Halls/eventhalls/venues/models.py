from django.db import models
from accounts.models import Venue

# Create your models here.

class VenueDetail(models.Model):
    max_guests = models.IntegerField()
    min_guests = models.IntegerField()
    recommended_tip = models.IntegerField()
    min_fee = models.IntegerField()
    outside_catering = models.BooleanField()
    venue_only_price = models.IntegerField(blank=True, null = True)
    deposit_fee = models.IntegerField()
    non_refundable_percent = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Kosher(models.Model):
    glatt = models.BooleanField()
    beit_yoseph = models.BooleanField()
    chalav_yisrael = models.BooleanField()
    kemach_yisrael = models.BooleanField()
    rabbinical_supervision = models.CharField(max_length=150, null=True, blank=True)
    dietary = models.OneToOneField('DietaryOption', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class JewishWedding(models.Model):
    seperate_seating_option = models.BooleanField()
    seperate_dancing_option = models.BooleanField()
    ichud_room = models.BooleanField()
    bride_reception_room = models.BooleanField()
    groom_ketubah_room = models.BooleanField()
    jewish = models.OneToOneField(Kosher, on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class SeaFood(models.Model):
    lobster = models.IntegerField()
    crab = models.IntegerField()
    shrimp = models.IntegerField()
    oysters = models.IntegerField()
    sea_food_package = models.IntegerField()
    dietary = models.OneToOneField('DietaryOption', on_delete=models.CASCADE)
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class DietaryOption(models.Model):
    vegitarian = models.BooleanField()
    vegan = models.BooleanField()
    gluten_free = models.BooleanField()
    lactose_free = models.BooleanField()
    halal = models.BooleanField()
    kosheroption = models.BooleanField()
    sea_food = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class FoodOption(models.Model):
    meat_meal = models.IntegerField()
    lamb_meal = models.IntegerField()
    fish_meal = models.IntegerField()
    meat_and_chicken = models.IntegerField()
    meat_and_fish = models.IntegerField()
    chicken_and_fish = models.IntegerField()
    vegitarian = models.IntegerField()
    vegan = models.IntegerField()
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    
class DrinkOption(models.Model):
    full_open_bar = models.ManyToManyField('Pricing', related_name='full_open_bar')
    bottom_shelf = models.ManyToManyField('Pricing', related_name='bottom_shelf')
    wine_and_beer = models.ManyToManyField('Pricing', related_name='wine_and_beer')
    wine_only = models.ManyToManyField('Pricing', related_name='wine_only')
    beer_only = models.ManyToManyField('Pricing', related_name='beer_only')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class MealOption(models.Model):
    buffet = models.BooleanField()
    sitdown = models.BooleanField()
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class WeddingCake(models.Model):
    two_layer = models.IntegerField()
    three_layer = models.IntegerField()
    four_layer = models.IntegerField()
    five_layer = models.IntegerField()
    cake = models.OneToOneField('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Tasting(models.Model):
    tasting_price = models.IntegerField()
    limitation = models.ForeignKey('Limitation', on_delete=models.CASCADE)
    pricing = models.ManyToManyField('Pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class CuttingTheCakeFee(models.Model):
    fee = models.IntegerField()
    limitation = models.OneToOneField('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    
class CorkFee(models.Model):
    fee = models.IntegerField()
    limitation = models.OneToOneField('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class ClosedBottleFee(models.Model):
    fee = models.IntegerField()
    limitation = models.ForeignKey('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Waiter(models.Model):
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    staff = models.ManyToManyField('Staff')

class Bartender(models.Model):
    cost_per_bartender = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    staff = models.ManyToManyField('Staff')

class OtherStaff(models.Model):
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)
    staff = models.ManyToManyField('Staff')

class CenterPiece(models.Model):
    provide_centerpieces = models.BooleanField()
    basic_pricing = models.ManyToManyField('Pricing', related_name='basic_pricing')
    custom_design = models.BooleanField()
    custom_pricing = models.ManyToManyField('Pricing', related_name='custom_pricing')
    outside_centerpieces_allowed = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class DanceFloor(models.Model):
    max_capacity = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PaymentMethod(models.Model):
    accept_check = models.BooleanField()
    accept_credit_card = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PaymentPlan(models.Model):
    months = models.IntegerField()
    last_payment_deadline = models.CharField(max_length=50, null=True, blank=True)
    limitation = models.ForeignKey('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class OutdoorOptions(models.Model):
    outdoor_reception = models.BooleanField()
    outdoor_ceremony = models.BooleanField()
    outdoor_dancing = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class RainBackUp(models.Model):
    tents_or_canopies = models.BooleanField()
    inside_space = models.BooleanField()
    electric_generator = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Overnight(models.Model):
    hotel_partners = models.BooleanField()
    room_costs = models.IntegerField()
    bulk_rooms_discount = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Parking(models.Model):
    onsite_parking = models.BooleanField()
    car_max = models.IntegerField()
    valet = models.BooleanField()
    valet_cost = models.IntegerField()
    parking_cost = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Rehearsal(models.Model):
    rehearsal_ceremonies = models.BooleanField()
    rehearsal_dinners = models.BooleanField()
    rehearsal_ceremony_cost = models.IntegerField()
    rehearsal_ceremony_pricing = models.ManyToManyField('Pricing', related_name='rehearsal_ceremony_pricing')
    rehearsal_dinner_cost = models.IntegerField()
    rehearsal_dinner_pricing = models.ManyToManyField('Pricing', related_name='rehearsal_dinner_pricing')
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class InsuranceAndRefund(models.Model):
    cancellation_insurance = models.BooleanField()
    insurance_partners = models.BooleanField()
    cancellation_insurance_cost = models.IntegerField()
    cancellation_policy_days = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class PhotoVideo(models.Model):
    inhouse_photography_cost = models.IntegerField()
    inhouse_video_cost = models.IntegerField()
    limitation = models.OneToOneField('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Flower(models.Model):
    custom_floral_design = models.BooleanField()
    custom_floral_pricing = models.ManyToManyField('Pricing', related_name='custom_floral_pricing')
    basic_florist_pricing = models.ManyToManyField('Pricing', related_name='basic_florist_pricing')
    limitation = models.ForeignKey('Limitation', on_delete=models.CASCADE)
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Decoration(models.Model):
    provide_decorations = models.BooleanField()
    decorations_pricing = models.ManyToManyField('Pricing')
    outside_decorations = models.BooleanField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class ArrivalSetUp(models.Model):
    hours_preevent_setup = models.IntegerField()
    hours_preevent_arrival = models.IntegerField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class EventDayContact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

class Limitation(models.Model):
    candles = models.BooleanField()
    sparklers = models.BooleanField()
    outside_photography = models.BooleanField()
    outside_videography = models.BooleanField()
    outside_florist = models.BooleanField()
    indoor_smoking = models.BooleanField()
    designated_smoking_area = models.BooleanField()
    secure_room = models.BooleanField()
    people_per_table = models.IntegerField()
    provide_booster_seats = models.BooleanField()
    provide_place_cards = models.BooleanField()
    offer_tastings = models.BooleanField()
    provide_wedding_cake = models.BooleanField()
    cake_cutting_fee = models.BooleanField()
    corkage_fee = models.BooleanField()
    unopen_bottle_fee = models.BooleanField()
    provide_waiters = models.BooleanField()
    provide_bartenders = models.BooleanField()
    payment_plans =  models.BooleanField()
    ceremony_reception_seperate_rooms = models.BooleanField()
    ceremony_seating_provided = models.BooleanField()
    tip_included = models.BooleanField()
    coat_room = models.BooleanField()
    wheelchair_accesible = models.BooleanField()
    other_limitations = models.TextField()
    other_notes = models.TextField()
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE)

class Pricing(models.Model):
    amount_of_people = models.IntegerField()
    cost = models.IntegerField()
    flat_fee = models.IntegerField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount_of_people} people for {self.cost} Dollars"

class Staff(models.Model):
    amount_of_people = models.IntegerField()
    amount_of_staff = models.IntegerField()
    flat_amount_staff = models.IntegerField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
