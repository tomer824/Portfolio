from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer, Venue

# Create your models here.

class Message(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
