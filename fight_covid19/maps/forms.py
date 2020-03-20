from fight_covid19.maps import models
from django import forms


class WellnessEntryForm(forms.ModelForm):
    class Meta:
        model = models.WellnessEntry
        fields = "__all__"
