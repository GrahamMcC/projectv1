from django import forms
from django.contrib.auth.models import User
from .models import Staff, Car, School, Faculty, Journey, User, Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ( 'user','schoolOfWork', 'driver', 'headOfSchool',
                  'head0fFaculty', 'uniManagement')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('model', 'colour', 'regNum', 'driver')

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('schoolName', 'headOfSchool', 'faculty')

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('facultyName', 'headOfFaculty')

class JourneyForm(forms.ModelForm):
    class Meta:
        model = Journey
        fields = ('car', 'origin', 'destination', 'dateOfJourney',
                  'departureTime', 'arrivalTime')


class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
