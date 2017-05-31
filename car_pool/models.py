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
    admin = models.BooleanField(default=False)
    homeCampus = models.ForeignKey('OriginOptions')


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



class DestinationOptions(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OriginOptions(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Journey(models.Model):
    reason = models.CharField(default="Why are you traveling",
                              max_length=20)
    car = models.ForeignKey('Car')
    origin = models.ForeignKey('OriginOptions')
    destination = models.ForeignKey('DestinationOptions') # add choices paramter
    dateOfJourney = models.DateField()
    departureTime = models.TimeField()
    arrivalTime = models.TimeField()
    available_seats = models.SmallIntegerField(default=5)
    distance = models.FloatField(default=0)
    cost_per_person = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)

    def get_distance(self):
        origin_name = self.origin.name
        destination_name = self.destination.name

        if origin_name == "Belfast" and destination_name == "Coleraine":
            self.distance = 56.7
        elif origin_name == "Coleraine" and destination_name == "Belfast":
            self.distance = 56.7
        elif origin_name == "Belfast" and destination_name == "Magee":
            self.distance = 71
        elif origin_name == "Magee" and destination_name == "Belfast":
            self.distance = 71
        elif origin_name == "Jordanstown" and destination_name == "Belfast":
            self.distance = 6.5
        elif origin_name == "Belfast" and destination_name == "Jordanstown":
            self.distance = 6.5
        elif origin_name == "Coleraine" and destination_name == "Magee" :
            self.distance = 31.5
        elif origin_name == "Magee" and destination_name == "Coleraine" :
            self.distance = 31.5
        elif origin_name == "Coleraine" and destination_name == "Jordanstown":
            self.distance = 56.2
        elif origin_name == "Jordanstown" and destination_name == "Coleraine":
            self.distance = 56.2
        elif origin_name == "Jordanstown" and destination_name == "Magee":
            self.distance = 69.2
        elif origin_name == "Magee" and destination_name == "Jordanstown":
            self.distance = 69.2

    def update_costs(self):
        seats_booked = self.car.numberOfSeats - self.available_seats
        if self.distance == 0:
            self.get_distance()
        self.total_cost = self.distance * 0.45
        if seats_booked == 0:
            seats_booked = 1
        self.cost_per_person = self.total_cost / seats_booked
        self.save()

    def on_create(self):
        self.get_distance()
        self.available_seats = 4
        self.update_costs()
        self.save()


    def book_seat(self, staffId):
        self.available_seats = self.available_seats - 1
        StaffJourney.objects.create(staffId= staffId, journeyId=self)
        self.update_costs()
        self.save()

    def __str__(self):
        journey = self.origin.name + " to " + self.destination.name + " on " + str(self.dateOfJourney)
        return journey

class StaffJourney(models.Model):
    staffId = models.ForeignKey('Staff')
    journeyId = models.ForeignKey('Journey')

    def __str__(self):
        StaffJourney = 'StaffJourney ' + str(self.pk)
        return StaffJourney
