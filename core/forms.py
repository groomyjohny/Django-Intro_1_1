from django import forms

from core import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.EmergencyServiceModel
        fields = '__all__'