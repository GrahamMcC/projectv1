from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schoolOfWork = models.TextField()
    driver = models.BooleanField()
    headOfSchool = models.BooleanField()
    head0fFaculty = models.BooleanField()
    uniManagement = models.BooleanField()

    def __str__(self):
        return self.user.username

class Car(models.Model):
    regNum = models.TextField()
    model = models.TextField()
    colour = models.TextField()
    driver = models.ForeignKey('Staff')
    numberOfSeats = models.IntegerField(default='0')


    def __str__(self):
        description = self.model + " " + self.colour
        return description

class Faculty(models.Model):
    facultyName = models.TextField()
    headOfFaculty = models.ForeignKey('Staff')

    def __str__(self):
        return self.facultyName

class School(models.Model):
    schoolName = models.TextField()
    faculty = models.ForeignKey('Faculty')
    headOfSchool = models.ForeignKey('Staff')

    def __str__(self):
        return self.schoolName


class Journey(models.Model):
    driver = models.ForeignKey('Staff')
    car = models.ForeignKey('Car')
    origin = models.TextField() # add chioces parameter
    destination = models.TextField() # add choices paramter
    dateOfJourney = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()

    def __str__(self):
        journey = self.destination + " to " + self.destination + " on " + self.dateOfJourney
        return journey
