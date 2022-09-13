from django.urls import path
from .views import *


app_name='dashboard'

urlpatterns =[
    path('commission/profile/', women_fellowship_base, name="women_base"),
    #temporary
    path('voting/candidate/add/',add_votting_candidate, name='add_candidate'),
    path('voting/vote/', get_voting_candidates, name='voting_candidates'),
    path('voting/add/vote/<str:national_id>/',add_vote, name='vote'),
    path('voting/results/', voting_results, name='voting_result'),
    path('group/members/',group_members, name='our_members'),
    path('add/meeting/',add_meeting, name='schedule_meeting'),
    path('private/meetings/',get_all_meetings, name='our_meetings'),
    path('services/add/',add_service, name='new_service'),
    path('church/services/',get_all_services, name='services'),
    path('general/church/services/',get_all_services1, name='general_services'),
 
]   