from django import forms
from .models import VenueDetail, DanceFloor, Tasting, Rehearsal, Decoration, ArrivalSetUp, Pricing, CenterPiece, Limitation, DrinkOption

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
    
class PricingForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['amount_of_people', 'cost']
    
PricingFormSet = forms.formset_factory(PricingForm, extra=1)