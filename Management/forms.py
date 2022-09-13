from django import forms
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from .models import Members


class MembersForm(forms.ModelForm):
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    national_id = forms.CharField(max_length=12)
    contact = forms.IntegerField()
    gender = forms.Select()
    commission = forms.Select()
    occupation = forms.CharField(max_length=25)
    leadership_position = forms.Select()
    location =forms.Select()
    marital_status = forms.Select()
    email = forms.EmailField()

    def clean_national_id(self):
        national_id = self.cleaned_data['national_id']
        national_id_format = re.compile(r"^\d{2}-\d{6}[a-zA-Z]{1}\d{2}$")
        pattern = national_id_format.search(national_id)
        if not pattern:
            raise ValidationError('Invalid national ID')
        if Members.objects.filter(national_id=national_id).exists():
            raise ValidationError('This national id is already used!')
        return national_id

    class Meta:
        model = Members
        fields = ['first_name','last_name','national_id','contact','gender','commission','occupation','leadership_position','location','marital_status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Enter Last Name'})
        self.fields['national_id'].widget.attrs.update(
            {'placeholder': 'e.g 74-560976G74'})
        self.fields['contact'].widget.attrs.update(
            {'placeholder': 'e.g 0775836222'})
        self.fields['gender'].widget.attrs.update(
            {'placeholder': '-select sex-'})
        self.fields['commission'].widget.attrs.update(
            {'placeholder': '-select commission-'})
        self.fields['occupation'].widget.attrs.update(
            {'placeholder': 'Enter Occupation'})
        self.fields['leadership_position'].widget.attrs.update(
            {'placeholder': '-select position-'})
        self.fields['location'].widget.attrs.update(
            {'placeholder': '-select location-'})
        self.fields['marital_status'].widget.attrs.update(
            {'placeholder': '-select status-'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Enter email address'})


class UserRegistration(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name','password1','password2']

    def clean_username(self):
        username = self.cleaned_data['username']
        r = User.objects.filter(username=username)
        if r.count():
            raise forms.ValidationError("Username already exists")
        
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        id = Members.objects.filter(national_id= first_name)
        if id.count() ==0:
            raise forms.ValidationError("Your National Id is not recognised!")
        return first_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control','Label':'Username','Placeholder':'Your username'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control','Label':'National Id','Placeholder':'Your national ID'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control','Placeholder':'Your password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control','Placeholder':'Confirm your password'})

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','Label':'Username:','Placeholder':'Your your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'Placeholder':'Your password'
        }
    ))


class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','Label':'Username:','Placeholder':'Your your username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'Placeholder':'Your password'
        }
    ))
