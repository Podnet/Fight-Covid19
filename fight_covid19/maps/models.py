from django.db import models
from django.contrib.auth import get_user_model


class HealthEntry(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    fever = models.BooleanField(default=False, null=True, blank=True)
    cough = models.BooleanField(default=False, null=True, blank=True)
    difficult_breathing = models.BooleanField(default=False, null=True, blank=True)
    self_quarantine = models.BooleanField(default=False, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=18, decimal_places=15, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=18, decimal_places=15, null=True, blank=True
    )
    creation_timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
