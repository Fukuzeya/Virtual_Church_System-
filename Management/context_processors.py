from .models import Members

def get_member(request):
    return {"member": Members.objects.get(national_id=request.user.first_name)}
