from django.urls import path
import core.views

urlpatterns = [
    path('views/1', core.views.accident_count_view),
    path('views/2', core.views.applicant_phone_number_view),
    path('views/3', core.views.redirect_src_view),
    path('views/redirect_dst', core.views.redirect_dst_view),
    path('views/4', core.views.rq_echo_view),
    path('views/5', core.views.user_data_by_phone_view),
    path('views/6/<int:uid>', core.views.user_json),

    path('all_applicants', core.views.all_applicants_view),
    path('all_applicants_numbered', core.views.all_applicants_numbered_view),
    path('all_accidents', core.views.all_accidents_view),
    path('all_appeals', core.views.all_appeals_view),

    path('', core.views.index_view),
    path('footer', core.views.footer_view),
    ]