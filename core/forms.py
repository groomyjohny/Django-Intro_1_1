from django import forms
from datetime import datetime
from core import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.EmergencyServiceModel
        fields = '__all__'
        help_texts = {
            'service_code': 'Здесь должен быть help-text, вот он',
        }


class ApplicantForm(forms.ModelForm):
    def clean(self):
        super().clean()

        if len(self.cleaned_data.get('phone_number')) > 11:
            self.errors['phone_number'] = self.error_class(['Номер телефона не должен содержать более 11 симоволов'])
        if self.cleaned_data.get('birth_date').year > datetime.now().year:
            self.errors['birth_date'] = self.error_class(['Год даты рождения не должен быть в будущем'])  # TODO: maybe should check whole date, not just year?

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
