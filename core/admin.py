from django.contrib import admin

import core.models
# Register your models here.
from core import models

@admin.register(core.models.EmergencyServiceModel)
class EmergencySeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serviceCode', 'phoneNumber')

@admin.register(core.models.ApplicantModel)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'phoneNumber', 'healthState')

@admin.register(core.models.AppealModel)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'applicantName')