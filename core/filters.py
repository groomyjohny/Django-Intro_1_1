import django_filters
from core import models


class ApplicantFilter(django_filters.FilterSet):
    class Meta:
        model = models.ApplicantModel
        exclude = ['image']
        fields = {
            'phone_number': ['icontains', 'exact'],
            'birth_date': ['lte', 'gte'],
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
