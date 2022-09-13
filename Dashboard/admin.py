from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Voting)
class VotingAdmin(admin.ModelAdmin):
    pass

@admin.register(Voting_Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


