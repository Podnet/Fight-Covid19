from django.db import models
from django.contrib.auth import get_user_model


class WellnessEntry(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    difficult_breathing = models.BooleanField(default=False)
    self_quarantine = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
