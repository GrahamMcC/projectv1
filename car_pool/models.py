from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

class Staff(models.Model):
    user = models.OneToOneField(User)
    schoolOfWork = models.ForeignKey('School')
    driver = models.BooleanField()
    headOfSchool = models.BooleanField()
    head0fFaculty = models.BooleanField()
    uniManagement = models.BooleanField()
    homeCampus = models.ForeignKey('Origin0ptions')


    def __str__(self):
        return self.user.username

class Car(models.Model):
    regNum = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    colour = models.CharField(max_length=20)
    driver = models.ForeignKey('Staff')
    numberOfSeats = models.IntegerField(default='5')

    def __str__(self):
        description = self.model + " " + self.colour
        return description


class Faculty(models.Model):
    facultyName = models.CharField(max_length=40)
    headOfFaculty = models.ForeignKey('Staff')

    def __str__(self):
        return self.facultyName


class School(models.Model):
    schoolName = models.CharField(max_length=30)
    faculty = models.ForeignKey('Faculty')
    headOfSchool = models.ForeignKey('Staff')

    def __str__(self):
        return self.schoolName

class Destination0ptions(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Origin0ptions(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Journey(models.Model):
    reason = models.CharField(default="Why are you traveling",
                              max_length=20)
    car = models.ForeignKey('Car')
    origin = models.ForeignKey('Origin0ptions')
    destination = models.ForeignKey('Destination0ptions') # add choices paramter
    dateOfJourney = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()
    available_seats = models.SmallIntegerField(default=4)

    def book_seat(self, staffId):
        self.available_seats = self.available_seats - 1
        StaffJourney.objects.create(staffId= staffId, journeyId=self)
        self.save()


    def __str__(self):
        self.available_seats = self.car.numberOfSeats -1
        journey = self.origin + " to " + self.destination + " on " + self.dateOfJourney
        return journey

class StaffJourney(models.Model):
    staffId = models.ForeignKey('Staff')
    journeyId = models.ForeignKey('Journey')

    def __str__(self):
        StaffJourney = 'StaffJourney ' + str(self.pk)
        return StaffJourney
