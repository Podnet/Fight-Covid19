from fight_covid19.maps import models
from django import forms


class HealthEntryForm(forms.ModelForm):
    class Meta:
        model = models.HealthEntry
        fields = [
            "fever",
            "cough",
            "difficult_breathing",
            "self_quarantine",
            "latitude",
            "longitude",
        ]
        labels = {
            "fever": "Do you have fever?",
            "cough": "Do you have Cough?",
            "difficult_breathing": "Do you have any difficulty in breathing?",
            "self_quarantine": "Have you self-quarantined yourself?",
            "latitude": "Latitude",
            "longitude": "Longitude",
        }
