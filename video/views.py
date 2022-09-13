from django.shortcuts import render
from Dashboard.models import Members
# Create your views here.
def main_view(request):
     person = Members.objects.get(national_id = request.user.first_name)
     #context ={}
     return render(request, 'main.html',{'group':person})


def general_service(request):
     if Members.objects.filter(national_id = request.user.first_name).exists():
          person = Members.objects.get(national_id = request.user.first_name)
     person = None
     #context ={}
     return render(request, 'general.html',{'group':person})