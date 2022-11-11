import datetime

import django_filters
from core import models
from django.db.models import Q, Count


class ApplicantNameSearchMixin:
    def applicant_full_name_filter(self, queryset, name, value, surname_field, first_name_field, middle_name_field, filter):
        # TODO: perhaps 'contains' search should force exact match for all fields except the last?
        total_q = Q()
        s = value.split(' ')
        sn, fn, mn = (i+'__'+filter for i in (surname_field, first_name_field, middle_name_field))

        if len(s) == 0:  # if nothing is inputted, no search is needed
            return queryset
        elif len(s) == 1:  # if there's one string, then search it in all 3 name fields
            total_q |= Q((sn, s[0])) | Q((fn, s[0])) | Q((mn, s[0]))
        elif len(s) == 2:  # if there are two strings, then search it in (Surname then First name) and (First name then Middle name)
            total_q |= \
                ( Q((sn, s[0])) & Q((fn, s[1])) ) | \
                ( Q((fn, s[0])) & Q((mn, s[1])) )
        elif len(s) == 3:  # if there are three strings, then search all of them in order
            total_q |= Q((sn, s[0])) & Q((fn, s[1])) & Q((mn, s[2]))
        else:
            return queryset.none()

        return queryset.filter(total_q)


class ApplicantFilter(django_filters.FilterSet, ApplicantNameSearchMixin):
    applicant_full_name_contains = django_filters.CharFilter(method='contains_method', label='ФИО заявителя содержит')
    applicant_full_name_exact = django_filters.CharFilter(method='exact_method', label='ФИО заявителя (точное)')
    birth_year_exact = django_filters.CharFilter(method='birth_year_exact_filter', label='Год рождения', max_length=4)

    def contains_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'surname', 'first_name', 'patronymic_name',
            'icontains')

    def exact_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'surname', 'first_name', 'patronymic_name',
            'exact')

    def birth_year_exact_filter(self, queryset, name, value):
        target_year = int(value)
        date_low = datetime.datetime(target_year, 1, 1)
        date_high = datetime.datetime(target_year+1, 1, 1)
        return queryset.filter(
            Q(birth_date__gte=date_low) & Q(birth_date__lt=date_high)
        )

    class Meta:
        model = models.ApplicantModel
        fields = ('phone_number', 'birth_year_exact', 'applicant_full_name_contains', 'applicant_full_name_exact')
        exclude = ('image',)


class AppealFilter(django_filters.FilterSet, ApplicantNameSearchMixin):
    applicant_full_name_contains = django_filters.CharFilter(method='applicant_contains_method', label="ФИО заявителя содержит")
    applicant_full_name_exact = django_filters.CharFilter(method='applicant_exact_method', label="ФИО заявителя (точное)")
    service_code_contains = django_filters.CharFilter(method='service_code_contains_filter', label='Код службы содержит')
    service_code_exact = django_filters.CharFilter(method='service_code_exact_filter', label='Код службы (точный)')

    def applicant_contains_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'applicant__surname', 'applicant__first_name', 'applicant__patronymic_name',
            'icontains')

    def applicant_exact_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'applicant__surname', 'applicant__first_name', 'applicant__patronymic_name',
            'exact')

    def service_code_contains_filter(self, queryset, name, value):
        return queryset.filter(services__service_code__icontains=value).distinct()

    def service_code_exact_filter(self, queryset, name, value):
        return queryset.filter(services__service_code__exact=value).distinct()

    class Meta:
        model = models.AppealModel
        fields = ('status', 'service_code_contains', 'service_code_exact', 'applicant_full_name_contains', 'applicant_full_name_exact')


class ApplicantNameFilter(django_filters.FilterSet, ApplicantNameSearchMixin):
    name_contains = django_filters.CharFilter(method='applicant_contains_method', label='ФИО заявителя содержит')
    name_exact = django_filters.CharFilter(method='applicant_exact_method', label='ФИО заявителя (точное)')
    appeals_count_range = django_filters.RangeFilter(method='appeals_count', label='Количество обращений')

    def applicant_contains_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'surname', 'first_name', 'patronymic_name',
            'icontains')

    def applicant_exact_method(self, queryset, name, value):
        return self.applicant_full_name_filter(
            queryset, name, value,
            'surname', 'first_name', 'patronymic_name',
            'exact')

    def appeals_count(self, queryset, name, value):
        qs = queryset.annotate(appeals_count=Count('appeals'))
        return qs.filter(appeals_count__range=(value.start, value.stop))
