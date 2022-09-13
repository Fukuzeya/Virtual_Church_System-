from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from paynow import Paynow
import time
from Management.models import Members
from .models import *

from Payments.forms import TransactionForm
# Create your views here.

paynow = Paynow(
    '14813', 
    '3e688baf-5630-4145-a99c-d5deb32e5b2e',
    'http://google.com', 
    'http://127.0.0.1:8000'
    )
#make payment
def make_payment(request):
    member = Members.objects.get(national_id = request.user.first_name)
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            _payment_type = form.cleaned_data['payment_type']
            _amount_paid = form.cleaned_data['amount_paid']
            _transaction_number = form.cleaned_data['transaction_number']
            try:
                payment = paynow.create_payment(_payment_type, 'samsonfukuzeya123@gmail.com')
                payment.add(_payment_type, _amount_paid)
                response = paynow.send_mobile(payment, str(_transaction_number), 'ecocash')
                if response.success:
                    poll_url = response.poll_url
                    print("Poll Url: ", poll_url)
                    status = paynow.check_transaction_status(poll_url)
                    time.sleep(30)
                    print("Payment Status: ", status.status)
                    transaction.member = member
                    transaction.save()
                    return redirect('payment:transaction_history')
                else:
                    messages.error(request,"Something went wrong with paynow server.")
                    return HttpResponseRedirect(reverse("payment:ecocash"))
            except:
                messages.error(request,"Something went wrong with paynow server, Check your transaction number!")
                return HttpResponseRedirect(reverse("payment:ecocash"))

    else:
        form = TransactionForm()
    return render(request,'groups/Women\'s Fellowship/make-payment.html',{'form':form})

def my_payment_history(request):
    member = Members.objects.get(national_id = request.user.first_name)
    transactions = Transaction.objects.filter(member = member)
    return render(request,'groups/Women\'s Fellowship/payment-history.html',{'transactions':transactions})


def pastor_make_payment(request):
    member = Members.objects.get(national_id = request.user.first_name)
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            _payment_type = form.cleaned_data['payment_type']
            _amount_paid = form.cleaned_data['amount_paid']
            _transaction_number = form.cleaned_data['transaction_number']
            try:
                payment = paynow.create_payment(_payment_type, 'samsonfukuzeya123@gmail.com')
                payment.add(_payment_type, _amount_paid)
                response = paynow.send_mobile(payment, str(_transaction_number), 'ecocash')
                if response.success:
                    poll_url = response.poll_url
                    print("Poll Url: ", poll_url)
                    status = paynow.check_transaction_status(poll_url)
                    time.sleep(30)
                    print("Payment Status: ", status.status)
                    transaction.member = member
                    transaction.save()
                    return redirect('management:members_payments')
                else:
                    messages.error(request,"Something went wrong with paynow server.")
                    return HttpResponseRedirect(reverse("management:members_payments"))
            except:
                messages.error(request,"Something went wrong with paynow server, Check your transaction number!")
                return HttpResponseRedirect(reverse("management:members_payments"))

    else:
        form = TransactionForm()
    return render(request,'pastor/make-payment.html',{'form':form})

    # payment = paynow.create_payment('Order', 'samsonfukuzeya123@gmail.com')
    # payment.add('Payment for stuff', 50)
    # response = paynow.send_mobile(payment, '0788751529', 'ecocash')
    # print(response)
    # if response.success:
    #     poll_url = response.poll_url
    #     print("Poll Url: ", poll_url)
    #     status = paynow.check_transaction_status(poll_url)
    #     time.sleep(30)
    #     print("Payment Status: ", status.status)
    #     return redirect('management:members')
    # else:
    #     return redirect('management:member_registration')



    # paynow_button = paynow.button_generator({
	# 	'email' : 'samsonfukuzeya123@gmail.com', # The Merchant's Email
	# 	'reference' : '123', # transaction reference
	# 	'amount' : 20.50, # transaction amount
	# 	'lock' : True, # Lock Form
	# 	'text' : 'donate', # Label for the button
	# 	'type' : 'image' # The type of button
	# 	})
	# context = {
	# 		'paynow_button' : paynow_button
	# 	}
	# return render(request, 'payment/index.html', context)











    
