import os
import sys
import django
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from car_pool.models import *


if __name__ == "__main__":

    journey_list = Journey.objects.all()
    for journey in journey_list:
        journey.delete()

    staffJourneys_list = StaffJourney.objects.all()
    for staffjourney in staffJourneys_list:
        staffjourney.delete()

    staff_list = Staff.objects.all()
    for staff in staff_list:
        if staff.user_id > 100:
            userID = staff.user_id
            user_object = User.objects.filter(id=userID)
            staff.delete()
            user_object.delete()

    """
    list_of_schools = School.objects.all()
    school_heads = {}
    for school in list_of_schools:
        staff_in_school = Staff.objects.filter(school=school)
        if len(staff_in_school) != 0:
            new_headOfSchool = random.choice(staff_in_school)
            new_headOfSchool.headOfSchool = True
            school.headOfSchool = new_headOfSchool
        else:
            print("no staff in school" + school.schoolName)
    """
