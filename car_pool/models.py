from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.TextField()
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
    driver = models.ForeignKey('auth.User')

    def __str__(self):
        description = self.model + " " + self.colour
        return description
