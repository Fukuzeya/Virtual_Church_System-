from turtle import position
from django.db import models

# Create your models here.
sex = (('Male','Male'),('Female','Female'),('Other','Other'))
mariatal_states = (('Married','Married'),('Single','Single'))
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
positions = (
    ('Elder','Elder'),
    ('Leader','Leader'),
    ('Chairperson','Chairperson'),
    ('Decon','Decon'),
    ('Secretary','Secretary'),
    ('Treasurer','Treasurer'),
    ('Member','Member'),
    ('Pastor','Pastor')
    )

locations = (
    ('Area 3','Area 3'),
    ('Area C','Area C'),
    ('Area 12','Area 12'),
    ('Area 13','Area 13'),
    ('Area 14','Area 14'),
    ('Area 16','Area 16'),
    ('Two Rooms','Two Rooms'),
    ('Destiny','Destiny')
    )
class Members(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    national_id = models.CharField(max_length=12,unique=True)
    contact = models.IntegerField()
    gender = models.CharField(max_length=25,choices=sex)
    commission = models.CharField(max_length=50,choices = commissions)
    occupation = models.CharField(max_length=25)
    leadership_position = models.CharField(max_length=25,choices=positions)
    location =models.CharField(max_length=25,choices=locations)
    marital_status = models.CharField(max_length=25,choices=mariatal_states)
    status = models.BooleanField(default=True)
    is_leader  = models.BooleanField(default=False)
    email = models.EmailField(max_length=100, null=True,blank=True)
    
