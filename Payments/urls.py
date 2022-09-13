from django.urls import path
from .views import *


app_name='payment'

urlpatterns =[
    path('online/payment',make_payment,name='ecocash'),
    path('paynow/payment',pastor_make_payment,name='pastor_ecocash'),
    path('transaction/history/',my_payment_history, name='transaction_history'),
]