from django.urls import path
import core.views.functional

urlpatterns = [
    path('views/1', core.views.functional.accident_count_view),
    path('views/2', core.views.functional.applicant_phone_number_view),
    path('views/3', core.views.functional.redirect_src_view),
    path('views/redirect_dst', core.views.functional.redirect_dst_view),
    path('views/4', core.views.functional.rq_echo_view),
    path('views/5', core.views.functional.user_data_by_phone_view),
    path('views/6/<int:uid>', core.views.functional.user_json),

    path('all_applicants', core.views.functional.all_applicants_view),
    path('all_applicants_numbered', core.views.functional.all_applicants_numbered_view),
    path('all_accidents', core.views.functional.all_accidents_view),
    path('all_appeals', core.views.functional.all_appeals_view),

    path('', core.views.functional.index_view),
    path('footer', core.views.functional.footer_view),
    ]