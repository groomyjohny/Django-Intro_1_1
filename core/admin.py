from django.contrib import admin

import core.models
# Register your models here.
from core import models


@admin.register(core.models.EmergencyServiceModel)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_code', 'phone_number')


@admin.register(core.models.ApplicantModel)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'birth_date', 'phone_number', 'health_state')


@admin.register(core.models.AppealModel)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'applicant_name', 'services_string')
