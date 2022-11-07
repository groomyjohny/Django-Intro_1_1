from django.urls import path
import core.views

urlpatterns = [
    path('views/1', core.views.AccidentCountView.as_view()),
    path('views/2', core.views.ApplicantPhoneNumberView.as_view()),
    path('views/3', core.views.redirect_src_view),
    path('views/redirect_dst', core.views.redirect_dst_view),
    path('views/4', core.views.RequestEchoView.as_view()),
    path('views/5', core.views.UserDataByPhoneView.as_view()),
    path('views/6/<int:uid>', core.views.user_json),

    path('all_applicants', core.views.AllApllicantsView.as_view()),
    path('all_applicants_numbered', core.views.all_applicants_numbered_view),
    path('all_accidents', core.views.all_accidents_view),
    path('all_appeals', core.views.all_appeals_view),

    path('', core.views.IndexView.as_view()),
    path('footer', core.views.FooterView.as_view()),
    ]