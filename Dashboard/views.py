import re
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import date
from Management.models import *
from .models import *
from .forms import *
from Payments.models import Transaction

# User.objects.distinct("first_name").all(),
# User.objects.all().order_by('-votes').first()
def publish_results(commission):
    voting_date = Voting_Candidate.objects.filter(commission = commission).first()
    if voting_date.end_date <= date.today():
        candidates = Voting_Candidate.objects.filter(commission=commission)
        winner = Voting_Candidate.objects.filter(commission=commission).order_by('-votes').first()
        print('====Winner======')
        print(winner.votes)
        member = Members.objects.get(national_id = winner.candidate)
        member.is_leader =True
        member.save()
        winner.has_won =True
        winner.save()
        for candidate in candidates:
            candidate.voting_closed =True
            candidate.save()
        
#women fellowship
def women_fellowship_base(request):
    user = Members.objects.get(national_id = request.user.first_name)
    members = Members.objects.all().count()
    group = Members.objects.filter(commission = user.commission).count()
    publish_results(user.commission)
    bal = 0
    transactions = Transaction.objects.filter(member = user)
    for trans in transactions:
        bal += trans.amount_paid
    return render(request, 'groups/Women\'s Fellowship/profile.html',{'user':user,'balance':bal,'members':members,'group':group})

def add_votting_candidate(request):
    if request.method =='POST':
        form = Voting_CandidateForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            national_id = form.cleaned_data['candidate']
            commission = form.cleaned_data['commission']
            if not Members.objects.filter(national_id = national_id, commission = commission).exists():
                messages.error(request,"Member is not under this commission!")
                return HttpResponseRedirect(reverse("dashboard:add_candidate"))
            user.save()
            messages.success(request,"Candidate registered successful!")
            return HttpResponseRedirect(reverse("dashboard:add_candidate"))
    else:
        form = Voting_CandidateForm()
    return render(request, 'management/add-candidate.html', {'form':form})

#List voting candidates
def get_voting_candidates(request):
    user = Members.objects.get(national_id = request.user.first_name)
    candidates = Voting_Candidate.objects.filter(commission = user.commission,voting_closed=False)
    return render(request, 'groups/Women\'s Fellowship/voting.html',{'candidates':candidates})

#Add vote
def add_vote(request,national_id):
    user = Members.objects.get(national_id = request.user.first_name)
    candidate = Voting_Candidate.objects.get(candidate = national_id)
    if Voting.objects.filter(member = user).exists():
        messages.error(request,"You cannot vote more than once!")
        return HttpResponseRedirect(reverse("dashboard:voting_candidates"))
    Voting.objects.create(member =user)
    candidate.votes +=1
    candidate.save()
    messages.success(request,"Vote casted successful!")
    return HttpResponseRedirect(reverse("dashboard:voting_candidates"))


#Voting results
def voting_results(request):
    user = Members.objects.get(national_id = request.user.first_name)
    candidates = Voting_Candidate.objects.filter(commission = user.commission).order_by('-votes')
    #arg = args.order_by('-rating').first() # may return None
    #arg = args.order_by('-rating')[0]
    
    return render(request, 'groups/Women\'s Fellowship/voting-results.html',{'candidates':candidates})

#Group members
def group_members(request):
    user = Members.objects.get(national_id = request.user.first_name)
    members = Members.objects.filter(commission = user.commission)
    return render(request,'groups/Women\'s Fellowship/members.html',{'members':members})

#add meeting
def add_meeting(request):
    person = Members.objects.get(national_id = request.user.first_name)
    if request.method =='POST':
        form = Private_MeetingForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.commission = person.commission
            user.leader = person
            user.save()
            messages.success(request,"Meeting scheduled successful")
            return HttpResponseRedirect(reverse("dashboard:schedule_meeting"))
    else:
        form = Private_MeetingForm()
    return render(request, 'groups/Women\'s Fellowship/add-meeting.html', {'form':form})

#view all meetings
def get_all_meetings(request):
    person = Members.objects.get(national_id = request.user.first_name)
    meetings = Private_Meetings.objects.filter(commission = person.commission)
    return render(request, 'groups/Women\'s Fellowship/meetings.html',{'meetings':meetings,'member':person})


def add_service(request):
    if request.method =='POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,"Service scheduled successful")
            return HttpResponseRedirect(reverse('dashboard:services'))
    else:
        form = ServiceForm()
    return render(request, 'pastor/add-service.html', {'form':form})


def get_all_services(request):
    services = GeneralServices.objects.all()
    return render(request, 'pastor/services.html',{'meetings':services})

def get_all_services1(request):
    services = GeneralServices.objects.all()
    return render(request, 'groups/Women\'s Fellowship/services.html',{'meetings':services})