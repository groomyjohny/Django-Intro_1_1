import datetime

import django_filters
from core import models
from django.db.models import Q


class ApplicantFilter(django_filters.FilterSet):
    applicant_full_name_contains = django_filters.CharFilter(method='applicant_full_name_contains_filter',
                                                          label="ФИО заявителя содержит")
    applicant_full_name_exact = django_filters.CharFilter(method='applicant_full_name_exact_filter',
                                                          label="ФИО заявителя (точное)")
    birth_year_exact = django_filters.CharFilter(method='birth_year_exact_filter', label='Год рождения', max_length=4)

    def applicant_full_name_contains_filter(self, queryset, name, value):
        return queryset.filter(
            Q(surname__icontains=value) | Q(first_name__icontains=value) | Q(patronymic_name__icontains=value)
        )

    def applicant_full_name_exact_filter(self, queryset, name, value):
        return queryset.filter(
            Q(surname__exact=value) | Q(first_name__exact=value) | Q(patronymic_name__exact=value)
        )

    def birth_year_exact_filter(self, queryset, name, value):
        target_year = int(value)
        date_low = datetime.datetime(target_year, 1, 1)
        date_high = datetime.datetime(target_year+1, 1, 1)
        return queryset.filter(
            Q(birth_date__gte=date_low) & Q(birth_date__lt=date_high)
        )

    class Meta:
        model = models.ApplicantModel
        fields = ['phone_number', 'birth_year_exact', 'applicant_full_name_contains', 'applicant_full_name_exact']
        exclude = ['image']
        #fields = ['applicant_full_name']
        #fields = {
        #    'phone_number': ['icontains', 'exact'],
        #    'birth_date': ['lte', 'gte'],
        #    'applicant_full_name': ['icontains', 'exact'],
        #    #'full_name': ['icontains', 'exact'],
        #}


class AppealFilter(django_filters.FilterSet):
    class Meta:
        model = models.AppealModel
        fields = {
            'status': ['exact'],
            'services__service_code': ['exact', 'contains'],
            #'applicant__full_name': ['exact', 'contains'],
        }
