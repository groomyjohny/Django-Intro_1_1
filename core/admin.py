from django.contrib import admin

import core.models
# Register your models here.
from core import models

@admin.register(core.models.EmergencyServiceModel)
class EmergencySeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serviceCode', 'phoneNumber')