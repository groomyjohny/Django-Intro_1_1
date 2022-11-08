import datetime

import django_filters
from core import models
from django.db.models import Q, Count


class ApplicantFilter(django_filters.FilterSet):
    applicant_full_name_contains = django_filters.CharFilter(method='applicant_full_name_contains_filter', label="ФИО заявителя содержит")
    applicant_full_name_exact = django_filters.CharFilter(method='applicant_full_name_exact_filter', label="ФИО заявителя (точное)")
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
    applicant_full_name_contains = django_filters.CharFilter(method='applicant_full_name_contains_filter', label="ФИО заявителя содержит")
    applicant_full_name_exact = django_filters.CharFilter(method='applicant_full_name_exact_filter', label="ФИО заявителя (точное)")
    service_code_contains = django_filters.CharFilter(method='service_code_contains_filter', label='Код службы содержит')
    service_code_exact = django_filters.CharFilter(method='service_code_exact_filter', label='Код службы (точный)')

    def applicant_full_name_contains_filter(self, queryset, name, value):
        return queryset.filter(
            Q(applicant__surname__icontains=value) |
            Q(applicant__first_name__icontains=value) |
            Q(applicant__patronymic_name__icontains=value)
        )

    def applicant_full_name_exact_filter(self, queryset, name, value):
        return queryset.filter(
            Q(applicant__surname__exact=value) |
            Q(applicant__first_name__exact=value) |
            Q(applicant__patronymic_name__exact=value)
        )

    def service_code_contains_filter(self, queryset, name, value):
        return queryset.filter(services__service_code__icontains=value).distinct()

    def service_code_exact_filter(self, queryset, name, value):
        return queryset.filter(services__service_code__exact=value).distinct()

    class Meta:
        model = models.AppealModel
        fields = ['status', 'service_code_contains', 'service_code_exact', 'applicant_full_name_contains', 'applicant_full_name_exact']
        #fields = {
        #    'status': ['exact'],
        #    'services__service_code': ['exact', 'contains'],
        #    #'applicant__full_name': ['exact', 'contains'],
        #}


class ApplicantNameFilter(django_filters.FilterSet):
    name_contains = django_filters.CharFilter(method='name_contains_filter', label="ФИО заявителя содержит")
    name_exact = django_filters.CharFilter(method='name_exacts_filter', label="ФИО заявителя (точное)")
    appeals_count_range = django_filters.RangeFilter(method='appeals_count', label='Количество обращений')

    def name_contains_filter(self, queryset, name, value):
        v = queryset.filter(
            Q(surname__icontains=value) |
            Q(first_name__icontains=value) |
            Q(patronymic_name__icontains=value)
        )
        return v

    def name_contains_exact(self, queryset, name, value):
        return queryset.filter(
            Q(surname__exact=value) |
            Q(first_name__exact=value) |
            Q(patronymic_name__exact=value)
        )


    def appeals_count(self, queryset, name, value):
        qs = queryset.annotate(appeals_count=Count('appeals'))
        return qs.filter(appeals_count__range=(value.start, value.stop))
