import os
import sys
import django
import random
import datetime
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
from car_pool.models import *

def namereader(fileName):
    with open(fileName,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        list_of_items = []
        for row in reader:
            list_of_items.append(row[0])

        return list_of_items

def carreader(fileName):
    with open(fileName,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        list_of_items = []
        for row in reader:
            list_of_items.append(row)

        return list_of_items


def report():
    global list_of_locations
    list_of_locations = OriginOptions.objects.all()
    list_of_dest = DestinationOptions.objects.all()
    global list_of_schools
    list_of_schools = School.objects.all()
    global list_of_users
    list_of_users = User.objects.all()
    global list_of_staff
    list_of_staff = Staff.objects.all()
    global list_of_drivers
    list_of_drivers = Staff.objects.filter(driver=True)
    global list_of_cars
    list_of_cars = Car.objects.all()

    print("locations:")
    print(list_of_locations)
    print("list_of_schools")
    print(list_of_schools)
    print("staff:")
    print(list_of_staff)
    print("drivers:")
    print(list_of_drivers)
    print("number of users")
    print(len(list_of_users))
    print("cars")
    print(list_of_cars)

def random_date():
    year = random.randint(2017,2018)
    months = random.randint(1, 12)

    if months == 8 or months == 4 or months == 6 or months == 10:
        day = random.randint(1,30)
    elif months == 2:
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)

    date = datetime.date(year, months, day)

    return date

def random_time():
    hours = random.randint(9, 17)
    mins = random.randrange(0, 45, 15)
    """
    if mins == 0:
        mins = '00'
    """
    time = datetime.time(hours, mins)
    return time


def create_staff(going_to_drive, staff_name):
    my_user = User.objects.create(username=staff_name, password='password1')
    school = random.choice(list_of_schools)
    campus = random.choice(list_of_locations)
    print(school)
    my_staff = Staff.objects.create(user= my_user,
                                    schoolOfWork= school,
                                    driver=going_to_drive,
                                    headOfSchool=False,
                                    head0fFaculty=False,
                                    uniManagement=False,
                                    homeCampus=campus)
    return my_staff

def create_car(my_staff, car_info):
    car_model = car_info[1]
    car_color = car_info[0]
    #random_regNum
    my_car = Car.objects.create(regNum="12fbbsgc",
                                model=car_model,
                                colour=car_color,
                                driver=my_staff,
                                numberOfSeats=4)
    return my_car


def create_journey(my_staff):
    origin = my_staff.homeCampus
    origin_name = origin.name
    print(origin_name)
    home = DestinationOptions.objects.get(name=origin_name)
    print(home)
    destination_list = []
    for location in list_of_dest:
        if location != home:
            destination_list.append(location)

    print(origin)
    print(destination_list)

    destination = random.choice(destination_list)
    #random date
    date = random_date() # format = YYYY-MM-DD
    # add number to date
    #random time between 9am and 5pm
    time = random_time()
    #calcualte arraival time
    arrival = time
    car_list = Car.objects.filter(driver= my_staff)
    my_jouney = Journey.objects.create(reason= "Procedurally generated reason",
                                       car= car_list[0],
                                       origin= origin ,
                                       destination= destination ,
                                       dateOfJourney= date,
                                       departureTime= time,
                                       arrivalTime= arrival )
    return my_jouney

if __name__ == "__main__":
    list_of_locations = OriginOptions.objects.all()
    list_of_dest = DestinationOptions.objects.all()
    list_of_schools = School.objects.all()
    list_of_users = User.objects.all()
    list_of_staff = Staff.objects.all()
    list_of_drivers = Staff.objects.filter(driver=True)
    list_of_cars = Car.objects.all()
    TorF = [True, True, False]
    names = namereader('names.csv')

    cars = carreader('cars.csv')
    report()

    number_name = len(names)
    for number in range(number_name):
        staff_name = names[number]
        car_info = cars[number]
        #create a number of users, subset being drivers
        going_to_drive = random.choice(TorF) # 50/50 is this ok??
        print(going_to_drive)

        my_staff = create_staff(going_to_drive, staff_name)
        report()

        if going_to_drive == True:
            my_car = create_car(my_staff, car_info)

        report()

    for driver in list_of_drivers:
        print(driver)
        if len(Car.objects.filter(driver= driver)) == 1:
            journey_counter = random.randrange(0,5)
            for number_of_j in range(journey_counter):
                journey = create_journey(driver)
                journey.on_create()
                passanger_counter = random.randrange(0,4)
                allreadybooked = []
                for passanger in range(passanger_counter):
                    passanger = random.choice(list_of_staff)
                    if passanger  not in allreadybooked:
                        allreadybooked.append(passanger)
                        journey.book_seat(passanger)
        else:
            print("didnt have car")
