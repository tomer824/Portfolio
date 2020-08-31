from django import forms
from .models import *

class VenueDetailForm(forms.ModelForm):
    class Meta:
        model = VenueDetail
        fields = ['max_guests', 'min_guests', 'min_fee', 'outside_catering', 'venue_only_price', 'deposit_fee', 'non_refundable_percent'
        ]
        labels = {
            'max_guests' : 'Max Guests',
            'min_guests' : 'Min Guests',
            'min_fee' : 'Min Fee',
            'outside_catering' : 'Outside Catering Permitted',
            'venue_only_price' : 'Venue Only Price',
            'deposit_fee' : 'Minimum Deposit Fee',
            'non_refundable_percent' : 'Deposit Non-Refundable Percent'
        }

class DanceFloorForm(forms.ModelForm):
    class Meta:
        model = DanceFloor
        fields = ['max_capacity']
        labels = {
            'max_capacity' : 'Dance Floor Max Capacity',
        }

class VenueDetailForm2(forms.ModelForm):
    class Meta:
        model = VenueDetail
        fields = ['recommended_tip']
        labels = {
            'recommended_tip' : 'Recommended Tip'
        }

class TastingForm(forms.ModelForm):
    class Meta:
        model = Tasting
        fields = ['tasting_price']
        labels = {
            'tasting_price' : 'Tasting Price'
        }

class RehearsalForm(forms.ModelForm):
    class Meta:
        model = Rehearsal
        fields = ['rehearsal_ceremonies', 'rehearsal_dinners', 'rehearsal_dinner_cost', 'rehearsal_ceremony_cost']
        labels = {
            'rehearsal_ceremonies' : 'Rehearsal Ceremony Option',
            'rehearsal_ceremony_cost' : 'Rehearsal Ceremony Cost',
            'rehearsal_dinners' : 'Rehearsal Dinner Option',
            'rehearsal_dinner_cost' : 'Rehearsal Dinner Cost',
        }

class DecorationForm(forms.ModelForm):
    class Meta:
        model = Decoration
        fields = ['decorations_pricing', 'outside_decorations', 'provide_decorations']
        labels = {
            'provide_decorations' : 'Provide Decorations',
            'decorations_pricing' : 'Cost of Basic Decorations',
            'outside_decorations' : 'Outside Decorations Permitted'
        }

class CenterPieceForm(forms.ModelForm):
    class Meta:
        model = CenterPiece
        fields = ['provide_centerpieces','basic_pricing', 'outside_centerpieces_allowed', 
        'custom_design', 'custom_pricing']
        labels = {
            'provide_centerpieces' : 'Venue Provides Basic Centerpiece Options',
            'basic_pricing' : 'Basic Centerpieces Cost',
            'outside_centerpieces_allowed' : 'Outside Centerpieces Permitted',
            'custom_design' : 'Custom Centerpiece Design Options',
            'custom_pricing' : 'Custom Centerpiece Design Average Cost',        
        }

class ArrivalSetUpForm(forms.ModelForm):
    class Meta:
        model = ArrivalSetUp
        fields = ['hours_preevent_setup', 'hours_preevent_arrival']
        labels = {
            'hours_preevent_arrival' : 'How Many Hours in Advance Can The Customer Arrive for Set Up',
            'hours_preevent_setup' : "How Many Hours in Advance Can the Customer Begin Setting Up"
        }

class DrinkOptionForm(forms.ModelForm):
    class Meta:
        model = DrinkOption
        fields = ['full_open_bar', 'bottom_shelf', 'wine_and_beer', 'wine_only', 
        'beer_only']
        labels = {
            'full_open_bar' : 'Full Open Bar',
            'bottom_shelf' : 'Bottom Shelf Only',
            'wine_and_beer' : 'Wine and Beer Only',
            'wine_only' : 'Wine Only',
            'beer_only' : 'Beer Only'
        }

class OutdoorOptionsForm(forms.ModelForm):
    class Meta: 
        model = OutdoorOptions
        fields = ['outdoor_reception', 'outdoor_ceremony', 'outdoor_dancing']
        labels = {
            'outdoor_reception' : 'Outdoor Reception Option',
            'outdoor_ceremony' : 'Outdoor Ceremony Option',
            'outdoor_dancing' : 'Outdoor Dance Floor Option'
        }

class IndoorOptionsForm(forms.ModelForm):
    class Meta: 
        model = IndoorOptions
        fields = ['indoor_reception', 'indoor_ceremony', 'indoor_dancing']
        labels = {
            'indoor_reception' : 'Indoor Reception Option',
            'indoor_ceremony' : 'Indoor Ceremony Option',
            'indoor_dancing' : 'Indoor Dance Floor Option'
        }

class OvernightForm(forms.ModelForm):
    class Meta:
        model = Overnight
        fields = ['hotel_partners', 'room_costs', 'bulk_rooms_discount']
        labels = {
           'hotel_partners' : 'Hotel Partners',
           'room_costs' : 'Room Costs',
           'bulk_rooms_discount' : 'Bulk Rooms Discount' 
        }

class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking
        fields = ['onsite_parking', 'car_max', 'valet', 'parking_cost']
        labels = {
            'onsite_parking' : 'Onsite Parking Available',
            'car_max' : 'Max No. of Cars in Parking Lot',
            'valet' : 'Valet Option',
            'parking_cost' : 'Cost of Parking / Valet'
        }

class AdditionalInformationForm(forms.ModelForm):
    class Meta:
        model = AdditionalInformation
        fields = ['candles', 'sparklers', 'indoor_smoking', 'designated_smoking_area', 'secure_room',
        'people_per_table', 'provide_booster_seats', 'provide_place_cards', 'ceremony_reception_seperate_rooms',
        'ceremony_seating_provided',]
        labels = {
            'candles' : 'Are candles allowed to be used',
            'sparklers' : 'Are sparklers allowed to be used',
            'indoor_smoking' : 'Is indoor smoking permitted',
            'designated_smoking_area' : 'Is there a designated smoking area',
            'secure_room' : 'Is there a secure room for gifts and storage',
            'people_per_table' : 'Average number of people seated per table',
            'provide_booster_seats' : 'Do you provide booster seats or other childrens seats',
            'provide_place_cards' : 'Do you provide place cards',
            'ceremony_reception_seperate_rooms' : 'Are the ceremony and reception held in separate rooms',
            'ceremony_seating_provided' : 'Do you provide seating for the ceremony',
            'tip_included' : 'Is the tip for the staff included in the price',
            'coat_room' : 'Do you have a coat room',
            'wheelchair_accesible' : 'Is the venue wheelchair accessible',
            'other_notes' : 'Other notes or comments'
        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['number_of_guests', 'number_of_waiters', 'number_of_bartenders', 'number_of_other_staff']
        labels = {
            'number_of_guests' : 'Number of Guests', 
            'number_of_waiters' : 'Number of Waiters',
            'number_of_bartenders' : 'Number of Bartenders',
            'number_of_other_staff' : 'Number of Other Staff'
        }


class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ['accept_check', 'accept_credit_card', 'wire_transfer', 'cash_only']
        labels = {
            'accept_check' : 'Accept Payment By Check',
            'accept_credit_card' : 'Accept Payment By Credit Card',
            'wire_transfer' : 'Accept Payment By Wire Transfer',
            'cash_only' : 'Accept Cash Only'
        }

class PaymentPlanForm(forms.ModelForm):
    class Meta:
        model = PaymentPlan
        fields = ['months', 'last_payment_deadline']
        labels = {
            'payment_plan_option' : 'Payment Plan Option Offered',
            'months' : 'Payment Plan Spread Over How Many Months',
            'last_payment_deadline' : 'Last Payment Due By'
        }

class EventDayContactForm(forms.ModelForm):
    class Meta:
        model = EventDayContact
        fields = ['name', 'phone', 'email']
        labels = {
            'name' : 'Contact Name',
            'phone'  : 'Cell Phone Number',
            'email' : 'Email'
        }

class GeneralContactForm(forms.ModelForm):
    class Meta:
        model = GeneralContact
        fields = ['contact_person', 'phone', 'email']
        labels = {
            'contact_person' : 'Name of Primary Contact',
            'phone' : 'General Phone Number',
            'email' : 'General Email Address'
        }

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['basic_florist_pricing', 'custom_floral_design', 'custom_floral_pricing', 'outside_florist']
        labels = {
            'basic_florist_pricing' : 'Cost of Basic In House Floral Arrangements',
            'custom_floral_design' : 'Custom Floral Arrangements Offered',
            'custom_floral_pricing' : 'Average Cost of Custom Floral Arrangements',
            'outside_florist' : 'Outside Floral Arrangements Permitted'
        }

class VenueImageForm(forms.ModelForm):
    class Meta:
        model = VenueImage
        fields = ['image']
        labels = {
            'image' : 'Upload Picture'
        }

class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['amount_of_people', 'cost']
        labels = {
            'amount_of_people' : 'Number of Guests',
            'cost' : 'Cost'
        }
    
PricingFormSet = forms.formset_factory(PricingForm, extra=1)


