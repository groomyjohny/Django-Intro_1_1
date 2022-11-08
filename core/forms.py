from django import forms

from core import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.EmergencyServiceModel
        fields = '__all__'


class ApplicantForm(forms.ModelForm):
    class Meta:
        model = models.ApplicantModel
        fields = '__all__'


class AppealForm(forms.ModelForm):
    class Meta:
        model = models.AppealModel
        fields = '__all__'
        help_texts = {
            'services': 'Нажмите и держите клавишу CTRL для выбора нескольких служб',
        }
