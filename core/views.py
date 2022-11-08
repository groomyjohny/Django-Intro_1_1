import json

from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg, Count
from django.views.generic import TemplateView, ListView, View, RedirectView
from django.core.exceptions import ObjectDoesNotExist

from core import models, forms
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
    url = '/core/views/redirect_dst' # TODO: hardcoded redirect


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


class CoreAddFormBase(TemplateView):
    form_type = None
    """Форма, которую будет обрабатывать эта View"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_type
        return context

    def post(self, request):
        form = self.form_type(request.POST)
        status_code = 400
        if form.is_valid():
            form.save()
            status_code = 201
            form = self.form_type
        return render(request, self.template_name, status=status_code, context={'form': form}) # form will be cleared if everything is OK, or sent back to user if not


class CoreEditFormBase(CoreAddFormBase):
    model = None
    def get(self, request, id):
        #id = int(request.GET['id'])
        try:
            obj = self.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse(f'Объекта с запрашиваемым ID ({id}) не существует', status=404)
        my_form = self.form_type(instance=obj)
        return render(request, self.template_name, status=200, context={'form': my_form})


class AddServiceView(CoreAddFormBase):
    template_name = 'add_service.html'
    form_type = forms.ServiceForm


class AddApplicantView(CoreAddFormBase):
    template_name = 'add_applicant.html'
    form_type = forms.ApplicantForm


class AddAppealView(CoreAddFormBase):
    template_name = 'add_appeal.html'
    form_type = forms.AppealForm


class AddAccidentView(CoreAddFormBase):
    template_name = 'add_accident.html'
    form_type = forms.AccidentForm


class EditServiceView(CoreEditFormBase):
    template_name = 'edit_service.html'
    form_type = forms.ServiceForm
    model = models.EmergencyServiceModel