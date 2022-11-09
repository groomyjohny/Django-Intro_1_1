import json

import django.urls
import django_filters.views
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg, Count
from django.views.generic import *
from django.core.exceptions import ObjectDoesNotExist

from core import models, forms, filters
# Create your views here.


class AccidentCountView(TemplateView):
    template_name = 'views_1.html'

    def get_context_data(self, **kwargs):
        count = models.AccidentModel.objects.count()
        if count == 0:
            raise Http404
        return {'count': count}


class ApplicantPhoneNumberView(TemplateView):
    template_name = 'views_2.html'

    def get_context_data(self, **kwargs):
        a_id = self.request.GET['id']
        phone = get_object_or_404(models.ApplicantModel, id=a_id).phone_number
        return {'phone': phone, 'id': a_id}


class RedirectDstView(TemplateView):
    template_name = "redirect_target.html"


class RedirectSrcView(RedirectView):
    url = '/core/views/redirect_dst'  # TODO: hardcoded redirect


class RequestEchoView(TemplateView):
    template_name = 'views_4.html'

    def get_context_data(self, **kwargs):
        return {'params': self.request.GET}


class UserDataByPhoneView(TemplateView):
    template_name = 'views_5.html'

    def get_context_data(self, **kwargs):
        phone = self.request.GET['phone']
        usr = models.ApplicantModel.objects.filter(phone_number=phone).values()[0]
        return {'user_in_a_list': [usr]}


class UserJsonView(View):
    def get(self, request, **kwargs):
        usr = models.ApplicantModel.objects.filter(id=kwargs.get('uid')).values()[0]
        return JsonResponse({'result': usr})


class IndexView(TemplateView):
    template_name = 'index.html'


class FooterView(TemplateView):
    template_name = 'footer.html'


class AllApllicantsView(ListView):
    model = models.ApplicantModel
    template_name = 'all_applicants.html'


class AllApllicantsNumberedView(ListView):
    model = models.ApplicantModel
    template_name = 'all_applicants_numbered.html'


class AllAccidentsView(ListView):
    model = models.AccidentModel
    template_name = 'all_accidents.html'


class AllAppealsView(ListView):
    model = models.AppealModel
    template_name = 'all_appeals.html'

    def get_context_data(self, **kwargs):
        appeals = self.model.objects.all()
        c = appeals.annotate(Count('services')).aggregate(Avg('services__count'))

        context = super().get_context_data(**kwargs)
        context['avg_service_count'] = c['services__count__avg']
        return context


class AddServiceView(CreateView):
    template_name = 'add_service.html'
    form_class = forms.ServiceForm
    success_url = 'add_service'


class AddApplicantView(CreateView):
    template_name = 'add_applicant.html'
    form_class = forms.ApplicantForm
    success_url = 'add_applicant'


class AddAppealView(CreateView):
    template_name = 'add_appeal.html'
    form_class = forms.AppealForm
    success_url = 'add_appeal'


class AddAccidentView(CreateView):
    template_name = 'add_accident.html'
    form_class = forms.AccidentForm
    success_url = 'add_accident'


class CoreUpdateView(UpdateView):
    fields = '__all__'
    success_url = '/core/success'


class EditServiceView(CoreUpdateView):
    template_name = 'edit_service.html'
    model = models.EmergencyServiceModel


class EditApplicantView(CoreUpdateView):
    template_name = 'edit_applicant.html'
    model = models.ApplicantModel


class EditAppealView(CoreUpdateView):
    template_name = 'edit_appeal.html'
    model = models.AppealModel


class FilterApplicantView(django_filters.views.FilterView):
    model = models.ApplicantModel
    template_name = 'filter_applicant.html'
    filterset_class = filters.ApplicantFilter


class FilterAppealView(django_filters.views.FilterView):
    model = models.AppealModel
    template_name = 'filter_appeal.html'
    filterset_class = filters.AppealFilter


class FilterApplicantNameView(django_filters.views.FilterView):
    model = models.ApplicantModel
    template_name = 'filter_applicant_name.html'
    filterset_class = filters.ApplicantNameFilter


class SuccessView(TemplateView):
    template_name = 'success.html'
