from django import forms

from .models import Staff, Car, School, Faculty

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ('user', 'schoolOfWork', 'driver', 'headOfSchool',
                  'head0fFaculty', 'uniManagement')


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
