import json

from django.http import JsonResponse, HttpResponse
from core import models, filters, forms
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Avg, Count


def accident_count_view(request):
    count = models.AccidentModel.objects.count()
    if count == 0:
        return HttpResponse(404)
    return render(request, "views_1.html", context={'count': count})


def applicant_phone_number_view(request):
    a_id = request.GET['id']
    phone = get_object_or_404(models.ApplicantModel, id=a_id).phone_number
    return render(request, "views_2.html", context={'phone': phone, 'id': a_id})


def redirect_src_view(request):
    return redirect(redirect_dst_view)


def redirect_dst_view(request):
    return render(request, 'redirect_target.html')


def rq_echo_view(request):
    return render(request, 'views_4.html', context={'params': request.GET})


def user_data_by_phone_view(request):
    phone = request.GET['phone']
    usr = models.ApplicantModel.objects.filter(phone_number=phone).values().first()

    return render(request, 'views_5.html', context={'user_in_a_list': [usr]})


def user_json(request, uid):
    usr = models.ApplicantModel.objects.filter(id=uid).values().first()

    return JsonResponse({'result': usr})


def index_view(request):
    return render(request, 'index.html')


def footer_view(request):
    return render(request, "footer.html")


def all_applicants_view(request):
    users = models.ApplicantModel.objects.all()
    return render(request, "all_applicants.html", context={'object_list': users})


def all_applicants_numbered_view(request):
    users = models.ApplicantModel.objects.all()
    return render(request, 'all_applicants_numbered.html', context={'object_list': users})


def all_accidents_view(request):
    accidents = models.AccidentModel.objects.all()
    return render(request, "all_accidents.html", context={'object_list': accidents})


def all_appeals_view(request):
    appeals = models.AppealModel.objects.all()
    c = appeals.annotate(Count('services')).aggregate(Avg('services__count'))
    return render(request, "all_appeals.html", context={'object_list': appeals, 'avg_service_count': c['services__count__avg']})


def add_accident(request):
    if request.method == 'GET':
        return render(request, 'add_accident.html', context={'form': forms.AccidentForm()})
    if request.method == 'POST':
        f = forms.AccidentForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request, 'add_accident.html', status=201, context={'form': forms.AccidentForm()})
        else:
            return render(request, 'add_accident.html', status=400, context={'form': f})


def add_appeal(request):
    if request.method == 'GET':
        return render(request, 'add_appeal.html', context={'form': forms.AppealForm()})
    if request.method == 'POST':
        f = forms.AppealForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request, 'add_appeal.html', status=201, context={'form': forms.AppealForm()})
        else:
            return render(request, 'add_appeal.html', status=400, context={'form': f})


def add_applicant(request):
    if request.method == 'GET':
        return render(request, 'add_applicant.html', context={'form': forms.ApplicantForm()})
    if request.method == 'POST':
        f = forms.ApplicantForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request, 'add_applicant.html', status=201, context={'form': forms.ApplicantForm()})
        else:
            return render(request, 'add_applicant.html', status=400, context={'form': f})


def add_service(request):
    if request.method == 'GET':
        return render(request, 'add_service.html', context={'form': forms.ServiceForm()})
    if request.method == 'POST':
        f = forms.ServiceForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request, 'add_service.html', status=201, context={'form': forms.ServiceForm()})
        else:
            return render(request, 'add_service.html', status=400, context={'form': f})


def edit_service(request, pk):
    obj = get_object_or_404(models.EmergencyServiceModel, id=pk)
    if request.method == 'GET':
        return render(request, 'edit_service.html', context={'form': forms.ServiceForm(instance=obj)})
    if request.method == 'POST':
        f = forms.ServiceForm(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return render(request, 'edit_service.html', status=201, context={'form': forms.ServiceForm()})
        else:
            return render(request, 'edit_service.html', status=400, context={'form': f})


def edit_applicant(request, pk):
    obj = get_object_or_404(models.ApplicantModel, id=pk)
    if request.method == 'GET':
        return render(request, 'edit_applicant.html', context={'form': forms.ApplicantForm(instance=obj)})
    if request.method == 'POST':
        f = forms.ApplicantForm(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return render(request, 'edit_applicant.html', status=201, context={'form': forms.ApplicantForm()})
        else:
            return render(request, 'edit_applicant.html', status=400, context={'form': f})


def edit_appeal(request, pk):
    obj = get_object_or_404(models.AppealModel, id=pk)
    if request.method == 'GET':
        return render(request, 'edit_appeal.html', context={'form': forms.AppealForm(instance=obj)})
    if request.method == 'POST':
        f = forms.AppealForm(request.POST, instance=obj)
        if f.is_valid():
            f.save()
            return render(request, 'edit_appeal.html', status=201, context={'form': forms.AppealForm()})
        else:
            return render(request, 'edit_appeal.html', status=400, context={'form': f})
