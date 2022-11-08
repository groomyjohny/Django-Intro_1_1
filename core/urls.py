from django.urls import path
import core.views

urlpatterns = [
    path('views/1', core.views.AccidentCountView.as_view()),
    path('views/2', core.views.ApplicantPhoneNumberView.as_view()),
    path('views/3', core.views.RedirectSrcView.as_view()),
    path('views/redirect_dst', core.views.RedirectDstView.as_view()),
    path('views/4', core.views.RequestEchoView.as_view()),
    path('views/5', core.views.UserDataByPhoneView.as_view()),
    path('views/6/<int:uid>', core.views.UserJsonView.as_view()),

    path('all_applicants', core.views.AllApllicantsView.as_view()),
    path('all_applicants_numbered', core.views.AllApllicantsNumberedView.as_view()),
    path('all_accidents', core.views.AllAccidentsView.as_view()),
    path('all_appeals', core.views.AllAppealsView.as_view()),

    path('add_service', core.views.AddServiceView.as_view()),
    path('add_applicant', core.views.AddApplicantView.as_view()),
    path('add_appeal', core.views.AddAppealView.as_view()),

    path('', core.views.IndexView.as_view()),
    path('footer', core.views.FooterView.as_view()),
    ]
