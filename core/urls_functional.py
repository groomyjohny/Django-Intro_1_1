from django.urls import path
import core.views.functional

urlpatterns = [
    path('view_1', core.views.functional.accident_count_view),
    path('view_2', core.views.functional.applicant_phone_number_view),
    path('view_3', core.views.functional.redirect_src_view),
    path('redirect_dst', core.views.functional.redirect_dst_view),
    path('view_4', core.views.functional.rq_echo_view),
    path('view_5', core.views.functional.user_data_by_phone_view),
    path('view_6/<int:uid>', core.views.functional.user_json),

    path('all_applicants', core.views.functional.all_applicants_view),
    path('all_applicants_numbered', core.views.functional.all_applicants_numbered_view),
    path('all_appeals', core.views.functional.all_appeals_view),

    path('add_appeal', core.views.functional.add_appeal),
    path('add_applicant', core.views.functional.add_applicant),
    path('add_service', core.views.functional.add_service),

    path('edit_service/<int:pk>', core.views.functional.edit_service),
    path('edit_applicant/<int:pk>', core.views.functional.edit_applicant),
    path('edit_appeal/<int:pk>', core.views.functional.edit_appeal),

    path('filter_applicant', core.views.functional.filter_applicant),
    path('filter_appeal', core.views.functional.filter_appeal),
    path('filter_applicant_name', core.views.functional.filter_applicant_activity),

    path('', core.views.functional.index_view),
    path('footer', core.views.functional.footer_view),
    ]
