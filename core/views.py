import json

from django.http import JsonResponse, HttpResponse

import core.models
from core import models
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg, Count
from django.views.generic import TemplateView, ListView
from django.http import Http404
# Create your views here.

class CoreViewException(Exception):
    pass


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


def redirect_src_view(request):
    return redirect(redirect_dst_view)


def redirect_dst_view(request):
    return render(request, 'redirect_target.html')


class RequestEchoView(TemplateView):
    template_name = 'views_4.html'

    def get_context_data(self, **kwargs):
        return {'params': self.request.GET}


class UserDataByPhoneView(TemplateView):
    template_name = 'views_5.html'

    def get_context_data(self, **kwargs):
        phone = self.request.GET['phone']
        usr = models.ApplicantModel.objects.filter(phone_number=phone).values()[0]
        return {'user_dict': usr}


def user_json(request, uid):
    usr = models.ApplicantModel.objects.filter(id=uid).values()[0]

    return JsonResponse({'result': usr})


class IndexView(TemplateView):
    template_name = 'index.html'


class FooterView(TemplateView):
    template_name = 'footer.html'


class AllApllicantsView(ListView):
    model = core.models.ApplicantModel
    template_name = 'all_applicants.html'


def all_applicants_view(request):
    users = models.ApplicantModel.objects.all()
    return render(request, "all_applicants.html", context={'users': users})


def all_applicants_numbered_view(request):
    users = models.ApplicantModel.objects.all()
    return render(request, 'all_applicants_numbered.html', context={'users': users})


def all_accidents_view(request):
    accidents = models.AccidentModel.objects.all()
    return render(request, "all_accidents.html", context={'accidents': accidents})


def all_appeals_view(request):
    appeals = models.AppealModel.objects.all()
    c = appeals.annotate(Count('services')).aggregate(Avg('services__count'))
    return render(request, "all_appeals.html", context={'appeals': appeals, 'avg_service_count': c['services__count__avg']})