from django import forms
from django.contrib.auth.models import User
from .models import Staff, Car, School, Faculty, Journey, User, Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('user', 'schoolOfWork', 'driver')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('regNum' ,'model', 'colour', 'driver', 'numberOfSeats')

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
        fields = ( 'reason','car', 'origin', 'destination', 'dateOfJourney',
                  'departureTime', 'arrivalTime')
        widgets = {
            'dateOfJourney': forms.DateInput(attrs={'class':'dateTime-input'}),
            'departureTime': forms.TimeInput(attrs={'class':'timepicker'}),
            'arrivalTime': forms.TimeInput(attrs={'class':'timepicker'})
        }

class loginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
