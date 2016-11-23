from django import forms

from .models import Car, School, Faculty

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ('model', 'colour', 'regNum', 'driver')

class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('schoolName', 'headOfSchool')

class facultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ('facultyName', 'headOfFaculty')
