# Generated by Django 3.1 on 2020-08-16 10:57

from django.db import migrations, models
import django.db.models.deletion
import venues.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegitarian', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('gluten_free', models.BooleanField()),
                ('lactose_free', models.BooleanField()),
                ('halal', models.BooleanField()),
                ('kosheroption', models.BooleanField()),
                ('sea_food', models.BooleanField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Limitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candles', models.BooleanField()),
                ('sparklers', models.BooleanField()),
                ('outside_photography', models.BooleanField()),
                ('outside_videography', models.BooleanField()),
                ('outside_florist', models.BooleanField()),
                ('indoor_smoking', models.BooleanField()),
                ('designated_smoking_area', models.BooleanField()),
                ('secure_room', models.BooleanField()),
                ('people_per_table', models.IntegerField()),
                ('provide_decorations', models.BooleanField()),
                ('provide_centerpieces', models.BooleanField()),
                ('provide_booster_seats', models.BooleanField()),
                ('provide_place_cards', models.BooleanField()),
                ('offer_tastings', models.BooleanField()),
                ('provide_wedding_cake', models.BooleanField()),
                ('cake_cutting_fee', models.BooleanField()),
                ('corkage_fee', models.BooleanField()),
                ('unopen_bottle_fee', models.BooleanField()),
                ('provide_waiters', models.BooleanField()),
                ('provide_bartenders', models.BooleanField()),
                ('payment_plans', models.BooleanField()),
                ('ceremony_reception_seperate_rooms', models.BooleanField()),
                ('ceremony_seating_provided', models.BooleanField()),
                ('tip_included', models.BooleanField()),
                ('coat_room', models.BooleanField()),
                ('wheelchair_accesible', models.BooleanField()),
                ('other_limitations', models.TextField()),
                ('other_notes', models.TextField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='WeddingCake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('two_layer', models.IntegerField()),
                ('three_layer', models.IntegerField()),
                ('four_layer', models.IntegerField()),
                ('five_layer', models.IntegerField()),
                ('cake', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='VenueDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_guests', models.IntegerField()),
                ('min_guests', models.IntegerField()),
                ('recommended_tip', models.IntegerField()),
                ('min_fee', models.IntegerField()),
                ('outside_catering', models.BooleanField()),
                ('venue_only_price', models.IntegerField(blank=True, null=True)),
                ('deposit_fee', models.IntegerField()),
                ('non_refundable_percent', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Tasting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasting_price', models.IntegerField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='SeaFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lobster', models.IntegerField()),
                ('crab', models.IntegerField()),
                ('shrimp', models.IntegerField()),
                ('oysters', models.IntegerField()),
                ('sea_food_package', models.IntegerField()),
                ('dietary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.dietaryoption')),
            ],
        ),
        migrations.CreateModel(
            name='Rehearsal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rehearsal_ceremonies', models.BooleanField()),
                ('rehearsal_dinners', models.BooleanField()),
                ('rehearsal_ceremony_cost', models.IntegerField()),
                ('rehearsal_dinner_cost', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='RainBackUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tents_or_canopies', models.BooleanField()),
                ('inside_space', models.BooleanField()),
                ('electric_generator', models.BooleanField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inhouse_photography_cost', models.IntegerField()),
                ('inhouse_video_cost', models.IntegerField()),
                ('limitation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('months', models.IntegerField()),
                ('last_payment_deadline', models.CharField(blank=True, max_length=50, null=True)),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_check', models.BooleanField()),
                ('accept_credit_card', models.BooleanField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onsite_parking', models.BooleanField()),
                ('car_max', models.IntegerField()),
                ('valet', models.BooleanField()),
                ('valet_cost', models.IntegerField()),
                ('parking_cost', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Overnight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_partners', models.BooleanField()),
                ('room_costs', models.IntegerField()),
                ('bulk_rooms_discount', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='OutdoorOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdoor_reception', models.BooleanField()),
                ('outdoor_ceremony', models.BooleanField()),
                ('outdoor_dancing', models.BooleanField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='MealOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buffet', models.BooleanField()),
                ('sitdown', models.BooleanField()),
                ('discounts', models.ManyToManyField(to='accounts.Discount')),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Kosher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glatt', models.BooleanField()),
                ('beit_yoseph', models.BooleanField()),
                ('chalav_yisrael', models.BooleanField()),
                ('kemach_yisrael', models.BooleanField()),
                ('dietary', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.dietaryoption')),
            ],
        ),
        migrations.CreateModel(
            name='JewishWedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seperate_seating_option', models.BooleanField()),
                ('seperate_dancing_option', models.BooleanField()),
                ('ichud_room', models.BooleanField()),
                ('bride_reception_room', models.BooleanField()),
                ('groom_ketubah_room', models.BooleanField()),
                ('jewish', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.kosher')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceAndRefund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancellation_insurance', models.BooleanField()),
                ('insurance_partners', models.BooleanField()),
                ('cancellation_insurance_cost', models.IntegerField()),
                ('cancellation_policy_days', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='FoodOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meat_meal', models.IntegerField()),
                ('lamb_meal', models.IntegerField()),
                ('fish_meal', models.IntegerField()),
                ('meat_and_chicken', models.IntegerField()),
                ('meat_and_fish', models.IntegerField()),
                ('chicken_and_fish', models.IntegerField()),
                ('vegitarian', models.IntegerField()),
                ('vegan', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_floral_design', models.BooleanField()),
                ('inhouse_florist_cost', models.IntegerField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='EventDayContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='DrinkOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullopenbar', models.IntegerField()),
                ('bottom_shelf', models.IntegerField()),
                ('wine_and_beer', models.IntegerField()),
                ('wine_only', models.IntegerField()),
                ('beer_only', models.IntegerField()),
                ('discounts', models.ManyToManyField(to='accounts.Discount')),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decorations_cost', models.IntegerField()),
                ('centerpieces_cost', models.IntegerField()),
                ('limitation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='DanceFloor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_capacity', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='CuttingTheCakeFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('limitation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='CorkFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('limitation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='ClosedBottleFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='CenterPiece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_design', models.BooleanField()),
                ('custom_design_cost', models.IntegerField()),
                ('external_center_pieces_allowed', models.BooleanField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Bartender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('cost_per_bartender', models.IntegerField()),
                ('total_bartender_charge', models.IntegerField()),
                ('limitation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.limitation')),
            ],
        ),
        migrations.CreateModel(
            name='ArrivalSetUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_preevent_setup', models.IntegerField()),
                ('hours_preevent_arrival', models.IntegerField()),
                ('venue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.venue')),
            ],
        ),
    ]
