import json

from django.http import JsonResponse, HttpResponse
from core import models
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

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
    return redirect('/views/redirect_dst')


def redirect_dst_view(request):
    return render(request, 'redirect_target.html')


def rq_echo_view(request):
    return render(request, 'views_4.html', context={'params': request.GET}) # TODO: remake!!!


def user_data_by_phone_view(request):
    phone = request.GET['phone']
    usr = models.ApplicantModel.objects.filter(phone_number=phone).values()[0]

    return render(request, 'views_5.html', context={'user_dict': usr}) # instead of just passing dict we can form it ourselves


def user_json(request, uid):
    usr = models.ApplicantModel.objects.filter(id=uid).values()[0]

    return JsonResponse({'result' : usr})
