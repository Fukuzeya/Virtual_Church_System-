from django.urls import path
from .views import general_service, main_view

app_name ='video'
urlpatterns = [
    path('',main_view, name="main"),
    path('general/service/',general_service, name='general_meeting'),
]
