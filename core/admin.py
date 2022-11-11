import datetime

from django.contrib import admin

import core.models
# Register your models here.
from core import models


@admin.register(core.models.EmergencyServiceModel)
class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_code', 'phone_number')
    empty_value_display = '(нет значения)'
    search_fields = ('name',)


class DecadeBornListFilter(admin.SimpleListFilter):
    title = 'Дата рождения'
    parameter_name = 'birth_year_range'

    def lookups(self, request, model_admin):
        return reversed(tuple(
            (f'{yr},{yr+10}', f'{yr}-{yr+9}') for yr in range(1900, datetime.datetime.now().year+1, 10)
        ))

    def queryset(self, request, queryset):
        if not self.value():
            return queryset

        yr_low, yr_high = [int(i) for i in self.value().split(',')]
        return queryset.filter(
            birth_date__gte=datetime.datetime(yr_low, 1, 1),
            birth_date__lt=datetime.datetime(yr_high, 1, 1)
        )


@admin.register(core.models.ApplicantModel)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'birth_date', 'phone_number', 'health_state')
    list_filter = ('gender', DecadeBornListFilter)
    empty_value_display = '(нет значения)'


@admin.register(core.models.AppealModel)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('date', 'number', 'card_number', 'status', 'applicant_name', 'injured_count', 'dont_call', 'services_string', 'description')
    readonly_fields = ('card_number',)
    empty_value_display = '(нет значения)'
    ordering = ('-date',)

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('number')
        return fields
