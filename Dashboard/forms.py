from django import forms
import re
from datetime import date
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date
from Management.models import Members

from .models import *


class Voting_CandidateForm(forms.ModelForm):
    candidate = forms.CharField(max_length=12)
    profile = forms.ImageField()
    commission  = forms.Select()
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Voting_Candidate
        fields = ['candidate','profile','commission','end_date']

    def clean_candidate(self):
        #check if the member exists in list of members
        _candidate = self.cleaned_data['candidate']
        national_id_format = re.compile(r"^\d{2}-\d{6}[a-zA-Z]{1}\d{2}$")
        pattern = national_id_format.search(_candidate)
        if not pattern:
            raise ValidationError('Invalid national ID')
        if not Members.objects.filter(national_id = _candidate).exists():
            raise ValidationError('Member is not recognised in our system!')
        if Voting_Candidate.objects.filter(candidate = _candidate).exists():
            raise ValidationError('Candidate Already registered!')
        return _candidate

    def clean_end_date(self):
        _end_date = self.cleaned_data['end_date'] 
        to_date = date.today()
        diff = _end_date - to_date
        diff_days = diff.days
        if diff_days < 0:
            raise ValidationError('Invalid date! Voting can only start atleast from today!')
        return _end_date

    def __inti__(self):
        super().__init__(*args, **kwargs)
        self.fields['candidate'].widget.attrs.update(
            {'class': 'form-control','Label':'national ID','Placeholder':'Candidate National ID'})
        self.fields['profile'].widget.attrs.update(
            {'class': 'form-control','Label':'Profile'})
        self.fields['commission'].widget.attrs.update(
            {'class': 'form-control','Label':'Commission'})
        self.fields['end_date'].widget.attrs.update(
            {'class': 'form-control','Label':'End date'})

class Private_MeetingForm(forms.ModelForm):
    meeting_title = forms.CharField(max_length=50)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    class Meta:
        model = Private_Meetings
        fields = ['meeting_title','date','time']

    def clean_date(self):
        _date = self.cleaned_data['date'] 
        to_date = date.today()
        diff = _date - to_date 
        diff_days =diff.days
        if diff_days < 0:
            raise ValidationError('Meeting can only start from today onwards.')
        return _date

    def __inti__(self):
        super().__init__(*args, **kwargs)
        self.fields['meeting_title'].widget.attrs.update(
            {'class': 'form-control','Label':'Title','Placeholder':'Meeting title'})
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control','Label':'Date'})
        self.fields['time'].widget.attrs.update(
            {'class': 'form-control','Label':'Time'})

class ServiceForm(forms.ModelForm):
    service_theme = forms.CharField(max_length=50)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.DateInput(attrs={'type': 'time'}))
    class Meta:
        model = GeneralServices
        fields = ['service_theme','date','time']

    def clean_date(self):
        _date = self.cleaned_data['date'] 
        to_date = date.today()
        diff = _date - to_date 
        diff_days =diff.days
        if diff_days < 0:
            raise ValidationError('Meeting can only start from today onwards.')
        return _date

    def __inti__(self):
        super().__init__(*args, **kwargs)
        self.fields['service_theme'].widget.attrs.update(
            {'class': 'form-control','Label':'Title','Placeholder':'Service theme'})
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control','Label':'Date'})
        self.fields['time'].widget.attrs.update(
            {'class': 'form-control','Label':'Time'})