from pyexpat import model
from datetime import date, time
from django.db import models
from Management.models import Members

# Create your models here.
commissions = (
    ('Women\'s Fellowship','Women\'s Fellowship'),
    ('Men\'s Fellowship','Men\'s Fellowship'),
    ('Youth\'s Fellowship','Youth\'s Fellowship'),
    ('Children\'s Ministry','Children\'s Ministry'),
    ('Couple\'s Ministry','Couple\'s Ministry'),
    ('Widows and Singles Ministry','Widows and Singles Ministry'),
    ('Intercession Team','Intercession Team'),
    ('Building Commission','Building Commission'),
    ('Fundraising Commission','Fundraising Commission'),
    ('Ushering Commision','Ushering Commision'),
    ('Praise Team','Praise Team'),
    ('Evangelism and Outreach Commission','Evangelism and Outreach Commission'),
    ('Health Commission','Health Commission'),
    ('Finance Commission','Finance Commission'),
    ('Pastor and Wife','Pastor and Wife'),
    ('Elders','Elders'),
    ('Decons and Deconnesses','Decons and Deconnesses')
)
#Voting table 
class Voting(models.Model):
    member = models.OneToOneField(Members, on_delete=models.DO_NOTHING, related_name='member_vote')
    date_voted = models.DateField(auto_now_add=True)


#voting results
class Voting_Candidate(models.Model):
    candidate = models.CharField(max_length=12)
    profile= models.ImageField(upload_to = "profiles", null=True, blank = True)
    commission  = models.CharField(max_length=50, choices = commissions)
    votes = models.IntegerField(default=0)
    has_won = models.BooleanField(default=False)
    end_date = models.DateField()
    voting_closed = models.BooleanField(default=False)


class Private_Meetings(models.Model):
    commission = models.CharField(max_length=100, choices = commissions)
    meeting_title = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    leader = models.ForeignKey(Members, on_delete=models.DO_NOTHING, related_name='meetings')

    def date_has_passed(self):
        return (self.date - date.today()).days < 0

    def meeting_date(self):
        return self.date > date.today()
            

class GeneralServices(models.Model):
    service_theme = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    
    def date_has_passed(self):
        return (self.date - date.today()).days < 0

    def meeting_date(self):
        return self.date > date.today()

class Meeting_Attendence(models.Model):
    member = models.ForeignKey(Members, on_delete=models.CASCADE, related_name='meeting_members')
    meeting = models.ForeignKey(Private_Meetings, on_delete=models.DO_NOTHING, related_name='private_meeting_members')
