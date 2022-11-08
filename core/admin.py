from django.contrib import admin

import core.models
# Register your models here.
from core import models


@admin.register(core.models.EmergencyServiceModel)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_code', 'phone_number')
    empty_value_display = '(нет значения)'
    search_fields = ['name']


@admin.register(core.models.ApplicantModel)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'birth_date', 'phone_number', 'health_state')
    empty_value_display = '(нет значения)'


@admin.register(core.models.AppealModel)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'card_number', 'status', 'applicant_name', 'services_string', 'description')
    readonly_fields = ('number', 'card_number')
    empty_value_display = '(нет значения)'


# admin.site.register(core.models.AccidentModel)
@admin.register(core.models.AccidentModel)
class AccidentAdmin(admin.ModelAdmin):
    list_display = ('number', 'addition_datetime', 'injured_count', 'dont_call', 'services_string')
    empty_value_display = '(нет значения)'
    ordering = ['-addition_datetime']

