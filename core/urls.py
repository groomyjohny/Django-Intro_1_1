from django.urls import path, include
import core.views.classed

urlpatterns = [
    path('functional/', include('core.urls_functional')),

    path('views/1', core.views.classed.AccidentCountView.as_view()),
    path('views/2', core.views.classed.ApplicantPhoneNumberView.as_view()),
    path('views/3', core.views.classed.RedirectSrcView.as_view()),
    path('views/redirect_dst', core.views.classed.RedirectDstView.as_view()),
    path('views/4', core.views.classed.RequestEchoView.as_view()),
    path('views/5', core.views.classed.UserDataByPhoneView.as_view()),
    path('views/6/<int:uid>', core.views.classed.UserJsonView.as_view()),

    path('all_applicants', core.views.classed.AllApllicantsView.as_view()),
    path('all_applicants_numbered', core.views.classed.AllApllicantsNumberedView.as_view()),
    path('all_accidents', core.views.classed.AllAccidentsView.as_view()),
    path('all_appeals', core.views.classed.AllAppealsView.as_view()),

    path('add_service', core.views.classed.AddServiceView.as_view()),
    path('add_applicant', core.views.classed.AddApplicantView.as_view()),
    path('add_appeal', core.views.classed.AddAppealView.as_view()),
    path('add_accident', core.views.classed.AddAccidentView.as_view()),

    path('edit_service/<int:pk>', core.views.classed.EditServiceView.as_view()),
    path('edit_applicant/<int:pk>', core.views.classed.EditApplicantView.as_view()),
    path('edit_appeal/<int:pk>', core.views.classed.EditAppealView.as_view()),

    path('filter_applicant', core.views.classed.FilterApplicantView.as_view()),
    path('filter_appeal', core.views.classed.FilterAppealView.as_view()),
    path('filter_applicant_name', core.views.classed.FilterApplicantNameView.as_view()),

    path('', core.views.classed.IndexView.as_view()),
    path('footer', core.views.classed.FooterView.as_view()),
    path('success', core.views.classed.SuccessView.as_view()),
    ]
