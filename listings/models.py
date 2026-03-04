from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    CATEGORY_CHOICES = [
        ('SALE', 'Sale'),
        ('RENT', 'Rent'),
        ('BUY', 'Buy'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    published = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return f"Inquiry by {self.user.username}"