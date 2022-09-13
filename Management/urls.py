from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm,AdminLoginForm
from .views import *


app_name='management'

urlpatterns =[
    path('',home_page, name='hom_page'),
    path('new/registration/', members_registration, name="member_registration"),
    path('main/entry/',home, name='entry'),
    path('members/',get_all_members, name="members"),
    path('member/account/',member_account, name='member_account'),
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html',form_class=UserLoginForm), name='login'),
    path('adminprofile/', auth_views.LoginView.as_view(template_name='management/admin-login.html',form_class=AdminLoginForm), name='adminlogin'),
    path('member/update/<int:id>/',update_member, name='member_update'),
    path('member/delete/<int:id>/',delete_member, name='member_delete'),
    path('reports/',reports, name='report'),
    path('pastor/profile/',pastor_portal, name='pastor_base'),
    path('members/all/',get_all_members_pastor, name='get_members'),
    path('members/payments/',get_members_payments, name='members_payments'),
   
]   