import django_filters
from core import models
from django.db.models import Q


class ApplicantFullNameTamer:

    def applicant_name_filter__contains(self, queryset, name, value):
        return queryset.filter(
            Q(surname__icontains=value) | Q(first_name__icontains=value) | Q(patronymic_name__icontains=value)
        )

    def applicant_name_filter__exact(self, queryset, name, value):
        return queryset.filter(
            Q(surname__exact=value) | Q(first_name__exact=value) | Q(patronymic_name__exact=value)
        )


class ApplicantFilter(django_filters.FilterSet, ApplicantFullNameTamer):
    applicant_full_name = django_filters.CharFilter(method='applicant_name_filter__contains', label="ФИО заявителя")
    class Meta:
        model = models.ApplicantModel
        exclude = ['image']
        #fields = ['applicant_full_name']
        fields = {
            'phone_number': ['icontains', 'exact'],
            'birth_date': ['lte', 'gte'],
            'applicant_full_name': ['icontains', 'exact'],
            #'full_name': ['icontains', 'exact'],
        }


class AppealFilter(django_filters.FilterSet):
    class Meta:
        model = models.AppealModel
        fields = {
            'status': ['exact'],
            'services__service_code': ['exact', 'contains'],
            #'applicant__full_name': ['exact', 'contains'],
        }
