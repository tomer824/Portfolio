from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Customer(models.Model):
    CHOICES = [('AL','Alabama'), ('AK','Alaska'), ('AZ', 'Arizona'), ('AR','Arkansas'), ('CA','California'), ('CO','Colorado'), ('CT','Connecticut'), ('DC','District of Columbia'), ('DE','Delaware'), ('FL','Florida'), ('GA','Georgia'), ('HI','Hawaii'), ('ID','Idaho'), ('IL','Illinois'), ('IN','Indiana'), ('IA','Iowa'), ('KS','Kansas'), ('KY','Kentucky'), ('LA','Louisiana'), ('ME','Maine'), ('MD','Maryland'), ('MA','Massachusetts'), ('MI','Michigan'), ('MN','Minnesota'), ('MS','Mississippi'), ('MO','Missouri'), ('MT','Montana'), ('NE','Nebraska'), ('NV','Nevada'), ('NH','New Hampshire'), ('NJ','New Jersey'), ('NM','New Mexico'), ('NY','New York'), ('NC','North Carolina'), ('ND','North Dakota'), ('OH','Ohio'), ('OK','Oklahoma'), ('OR','Oregon'), ('PA','Pennsylvania'), ('RI','Rhode Island'), ('SC','South Carolina'), ('SD','South Dakota'), ('TN','Tennessee'), ('TX','Texas'), ('UT','Utah'), ('VT','Vermont'), ('VA','Virginia'), ('WA','Washington'), ('WV','West Virginia'), ('WI','Wisconsin'), ('WY','Wyoming')]
    phone_number = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20, choices = CHOICES)
    zipcode = models.CharField(max_length=5)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.get_full_name()

class Venue(models.Model):
    CHOICES = [('AL','Alabama'), ('AK','Alaska'), ('AZ','Arizona'), ('AR','Arkansas'), ('CA','California'), ('CO','Colorado'), ('CT','Connecticut'), ('DC','District of Columbia'), ('DE','Delaware'), ('FL','Florida'), ('GA','Georgia'), ('HI','Hawaii'), ('ID','Idaho'), ('IL','Illinois'), ('IN','Indiana'), ('IA','Iowa'), ('KS','Kansas'), ('KY','Kentucky'), ('LA','Louisiana'), ('ME','Maine'), ('MD','Maryland'), ('MA','Massachusetts'), ('MI','Michigan'), ('MN','Minnesota'), ('MS','Mississippi'), ('MO','Missouri'), ('MT','Montana'), ('NE','Nebraska'), ('NV','Nevada'), ('NH','New Hampshire'), ('NJ','New Jersey'), ('NM','New Mexico'), ('NY','New York'), ('NC','North Carolina'), ('ND','North Dakota'), ('OH','Ohio'), ('OK','Oklahoma'), ('OR','Oregon'), ('PA','Pennsylvania'), ('RI','Rhode Island'), ('SC','South Carolina'), ('SD','South Dakota'), ('TN','Tennessee'), ('TX','Texas'), ('UT','Utah'), ('VT','Vermont'), ('VA','Virginia'), ('WA','Washington'), ('WV','West Virginia'), ('WI','Wisconsin'), ('WY','Wyoming')]
    hall_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20, choices = CHOICES)
    zipcode = models.CharField(max_length=5)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.hall_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.hall_name + str(self.id))
        super(Venue, self).save(*args, **kwargs)
