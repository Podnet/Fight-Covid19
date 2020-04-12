from django.db import models
from django.contrib.auth import get_user_model


class HealthEntry(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    age = models.IntegerField(default=0)
    gender = models.CharField(
        choices=(("M", "Male"), ("F", "Female")), default="M", max_length=1,
    )
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    difficult_breathing = models.BooleanField(default=False)
    self_quarantine = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
    unique_id = models.CharField(null=True, blank=True, max_length=15)
    creation_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class KeyValuePair(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)


class HelpEntry(models.Model):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    help_type = models.CharField(
        choices=(
            ("food_donation", "Food Donation"),
            ("grocery_store", "Grocery Store"),
            ("medical_store", "Medical Store"),
            ("other", "Other"),
        ),
        default="food_donation",
        max_length=10,
    )
    address = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=15, null=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
