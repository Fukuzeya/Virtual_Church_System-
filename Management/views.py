from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Count

from Payments.models import Transaction
from .forms import MembersForm,UserRegistration
from .models import Members
# Create your views here.

#home page
def home_page(request):
    return render(request,'index.html')


def is_Pastor(user):
    return user.groups.filter(name='Pastor and Wife').exists()
def is_Womens_Fellowship(user):
    return user.groups.filter(name='Women\'s Fellowship').exists()
def is_admin(user):
    return user.groups.filter(name='Admins').exists()


@login_required
def home(request):
    if is_admin(request.user):
        return redirect('management:members')
    elif is_Pastor(request.user):
        return redirect('management:pastor_base')
    else:
        return redirect('dashboard:women_base')

#pastor profile page
def pastor_portal(request):
    user = Members.objects.get(national_id = request.user.first_name)
    members = Members.objects.all().count()
    return render(request, 'pastor/profile.html',{'user':user,'members':members})


#member account
def member_account(request):
    if request.method =='POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            id = form.cleaned_data['first_name']
            member = Members.objects.get(national_id=id)
            group  = Group.objects.get(name=member.commission)
            user.save()
            group.user_set.add(user)
            return redirect('management:login')
    else:
        form = UserRegistration()
    return render(request,'management/signup.html',{'form':form})

#Members registration
def members_registration(request):
    #group  = Group.objects.get(name="Users")
    if request.method =='POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            commission = form.cleaned_data['commission']
            #group  = Group.objects.get(name=commission)
            member.save()
            #group.user_set.add(user)
            return redirect('management:members')
    else:
        form = MembersForm()
    return render(request,'management/commission-registration.html',{'form':form})

#list of members
def get_all_members(request):
    members = Members.objects.all()
    return render(request,'management/members.html',{'members':members})

#list of members for pastor
def get_all_members_pastor(request):
    members = Members.objects.all()
    return render(request,'pastor/members.html',{'members':members})


#Members registration
def update_member(request,id):
    member = Members.objects.get(id=id)
    form = MembersForm(instance = member)
    if request.method =='POST':
        form = MembersForm(request.POST, instance =member)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()

            return redirect('management:members')
    return render(request,'management/commission-registration.html',{'form':form})

#delete member
def delete_member(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return redirect("management:members")

def reports(request):
    youth = Members.objects.filter(commission = 'Youth\'s Fellowship').count()
    men = Members.objects.filter(commission = 'Men\'s Fellowship').count()
    women = Members.objects.filter(commission = 'Women\'s Fellowship').count()
    decons = Members.objects.filter(commission = 'Decons and Deconnesses').count()
    
    commission_list = ['Youth Fellowship','Men Fellowship','Women Fellowship']
    number_list = [int(youth),int(men),int(women)]
    context ={'commission_list':commission_list,'number_list':number_list}
    return render(request, 'management/reports.html',context)


def get_members_payments(request):
    payments = Transaction.objects.all().annotate(Count('member')).order_by('transaction_date')
    return render(request, 'pastor/payment-history.html',{'transactions':payments})