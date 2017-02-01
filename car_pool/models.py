from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.ForeignKey(User)
    schoolOfWork = models.ForeignKey('School')
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
    facultyName = models.TextField(max_length=40)
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
    reason = models.TextField(default="please give a reason for the journey",
                              max_length=30)
    car = models.ForeignKey('Car')
    origin = models.TextField() # add chioces parameter
    destination = models.TextField() # add choices paramter
    dateOfJourney = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()

    def book_seat():
        self.seats = self.car.numberOfSeats - 1

    def __str__(self):
        journey = self.origin + " to " + self.destination + " on " + self.dateOfJourney
        self.seats = self.car.numberOfSeats
        return journey

class StaffJourney(models.Model):
    staffId = models.ForeignKey('Staff')
    JourneyId = models.ForeignKey('Journey')
