from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import datetime

#functions to get a sub set of journeys

def get_journey_from_id(id):
	current_journey = Journey.objects.get(pk=id)
	return current_journey

def get_passenger_list(journey):
	staffJourneys_list = StaffJourney.objects.filter(journeyId=journey)
	passenger_list = []
	for staffjourney in staffJourneys_list:
		passenger_list.append(staffjourney.staffId)
	return passenger_list

def user_equals_driver(staff_object):
	if staff_object.driver == True:
		drivers_car = Car.objects.filter(driver=staff_object)
		journey_list = Journey.objects.filter(car=drivers_car)
	else:
		 journey_list= []
	return journey_list

def user_equals_passenger(staff_object):
	staffJourneys_list = StaffJourney.objects.filter(staffId=staff_object)
	jobject_list = []
	for staffJourney in staffJourneys_list:
		myjourney = get_journey_from_id(staffJourney.journeyId_id)
		jobject_list.append(myjourney)
	return jobject_list


def get_staff_in_school(school):
	list_of_staff  = Staff.objects.filter(schoolOfWork=school)
	return list_of_staff

def get_schools_in_faculty(faculty_object):
	list_of_schools = School.objects.filter(faculty=faculty_object)
	return list_of_schools


def report_single_staff(staff):
	journeys_driven = user_equals_driver(staff)
	journeys_passanger = user_equals_passenger(staff)

	staff.total_traveled = len(journeys_passanger) + len(journeys_driven)
	staff.driven_for = len(journeys_driven)
	staff.passenger_for = len(journeys_passanger)

	staff.distance_driven = 0
	staff.reduced_cost = 0
	staff.total_cost = 0
	staff.distance_passenger = 0

	for journey in journeys_driven:
		staff.distance_driven = journey.distance + staff.distance_driven
		staff.reduced_cost = staff.reduced_cost + journey.cost_per_person
		staff.total_cost = staff.total_cost + journey.total_cost

	for journey in journeys_passanger:
		staff.distance_passenger = journey.distance + staff.distance_driven
		staff.reduced_cost = staff.reduced_cost + journey.cost_per_person
		staff.total_cost = staff.total_cost + journey.total_cost

	staff.total_distance =	staff.distance_driven + staff.distance_passenger
	staff.saving = staff.total_cost - staff.reduced_cost

	return staff

def update_list_of_staff(list_of_staff):
	updated_staff_list = []

	for staff in list_of_staff:
		updated_staff = report_single_staff(staff)
		updated_staff_list.append(updated_staff)

	return updated_staff_list

def update_list_of_schools(list_of_schools):
	updated_school_list = []

	for school in list_of_schools:
		list_of_staff = get_staff_in_school(school)

		updated_staff_list = update_list_of_staff(list_of_staff)
		updated_school = update_object(school,  updated_staff_list)
		updated_school_list.append(updated_school)

	return updated_school_list


def update_list_of_faculty(list_of_faculity):
	updated_faculty_list = []

	for faculty in list_of_faculity:
		list_of_schools = get_schools_in_faculty(faculty)
		updated_school_list = update_list_of_schools(list_of_schools)
		updated_faculty =  update_object(faculty, updated_school_list)
		updated_faculty_list.append(updated_faculty)

	return updated_faculty_list


def update_object(item, component_list):
	item.total_traveled = 0
	item.driven_for = 0
	item.passenger_for = 0

	item.distance_driven = 0
	item.distance_passenger = 0
	item.reduced_cost = 0
	item.total_cost = 0

	item.total_distance = 0
	item.saving = 0

	for component in component_list:
		item.total_traveled = item.total_traveled + component.total_traveled
		item.driven_for = item.driven_for + component.driven_for
		item.passenger_for = item.passenger_for + component.passenger_for

		item.distance_driven = item.distance_driven + component.distance_driven
		item.distance_passenger = item.distance_passenger + component.distance_passenger
		item.reduced_cost = item.reduced_cost + component.reduced_cost
		item.total_cost = item.total_cost + component.total_cost

	item.total_distance = item.distance_driven + item.distance_passenger
	item.saving = item.total_cost - item.reduced_cost

	return item
"""
def update_faculty(faculty, school_list):
"""

@login_required(login_url='/login/')
def reports(request, pk):
	if pk == '1':
		staff = request.user.staff
		staff = report_single_staff(staff)
		user_is_driver = user_equals_driver(staff)
		user_is_passenger = user_equals_passenger(staff)
		return render(request, 'car_pool/my_reports.html', {'staff': staff,
															'user_is_driver': user_is_driver,
															'user_is_passenger': user_is_passenger})
	elif pk == '2':
		school = request.user.staff.schoolOfWork
		list_of_staff = get_staff_in_school(school)
		updated_staff_list = update_list_of_staff(list_of_staff)
		updated_school = update_object(school,  updated_staff_list)

		return render(request, 'car_pool/school_reports.html', {'school': updated_school,
															  	'staff_list': updated_staff_list})
	elif pk == '3':
		faculty = request.user.staff.schoolOfWork.faculty
		list_of_schools = get_schools_in_faculty(faculty)
		updated_school_list = update_list_of_schools(list_of_schools)
		updated_faculty =  update_object(faculty, updated_school_list)

		return render(request, 'car_pool/faculty_reports.html', {'faculty': updated_faculty,
															  	 'school_list': updated_school_list})
	elif pk == '4':
		university = type('uni', (), {})()
		list_of_faculity = Faculty.objects.all()
		updated_faculty_list = update_list_of_faculty(list_of_faculity)
		update_university = update_object(university, updated_faculty_list)

		return render(request, 'car_pool/uni_reports.html', {'uni': university,
															  'faculty_list': updated_faculty_list})

#functions to login
def login(request):
	#https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
	return render(request, 'car_pool/log_in.html')

#function for forgot password
def forgot_password(request):
	return render(request, 'car_pool/log_in.html')


@login_required(login_url='/login/')
def admin(request):
	return render(request, 'car_pool/admin.html')

@login_required(login_url='/login/')
def my_info(request):
	#get_users_car
	if request.user.staff.driver == True:
		users_car = Car.objects.filter(driver=request.user.staff)
		try:
			car = users_car[0]
		except:
			TempCar = Car.objects.filter(id=666)
			car = TempCar[0]

	else:
		car = False
	#get list of journeys where user is driver
	user_is_driver = user_equals_driver(request.user.staff)
	#get list of journeys where user is passenger
	user_is_passenger = user_equals_passenger(request.user.staff)
	return render(request, 'car_pool/my_info.html', {'car': car,
													'user_is_driver': user_is_driver,
													'user_is_passenger':user_is_passenger})

#fuctions to return a list of instances
@login_required(login_url='/login/')
def staff_list(request):
	staff = Staff.objects.all()
	return render(request, 'car_pool/staff_list.html',
						   {'staff': staff})

@login_required(login_url='/login/')
def car_list(request):
	car_list = Car.objects.all()
	return render(request, 'car_pool/car_list.html',
						   {'car_list': car_list})

@login_required(login_url='/login/')
def faculty_list(request):
	faculty_list =  Faculty.objects.all()
	for faculty in faculty_list:
		list_of_schools = School.objects.filter(faculty=faculty.pk)
		faculty.list_of_schools = list_of_schools
	return render(request, 'car_pool/faculty_list.html',
						   {'faculty_list': faculty_list})

@login_required(login_url='/login/')
def school_list(request):
	school_list =  School.objects.all()
	return render(request, 'car_pool/school_list.html',
						   {'school_list': school_list})

@login_required(login_url='/login/')
def journey_list(request):
	journey_list = Journey.objects.order_by('dateOfJourney').filter(origin=request.user.staff.homeCampus)
	my_journey_list = []
	for journey in journey_list:
		if journey.available_seats > 0:
			journey.passenger_list = get_passenger_list(journey)
			my_journey_list.append(journey)
	return render(request, 'car_pool/journey_list.html',
							{'journey_list': my_journey_list })

@login_required(login_url='/login/')
def journey_selection(request, pk):
		if pk == 0:
			location = user.staff.homeCampus
		else:
			location = OriginOptions.objects.filter(id=pk)

		journey_list = Journey.objects.order_by('dateOfJourney').filter(origin=location)
		my_journey_list = []
		for journey in journey_list:
			if journey.available_seats > 0:
				journey.passenger_list = get_passenger_list(journey)
				my_journey_list.append(journey)

		return render(request, 'car_pool/journey_list.html',
								{'journey_list': my_journey_list })

# funtions to look at an instance in more detail
@login_required(login_url='/login/')
def car_detail(request, pk):
	car = get_object_or_404(Car, pk=pk)
	return render(request, 'car_pool/car_detail.html', {'car': car})

@login_required(login_url='/login/')
def journey_detail(request, pk):
	journey = get_object_or_404(Journey, pk=pk)
	staffjourney = StaffJourney.objects.filter(journeyId=journey)
	staffids = []
	for staffj in staffjourney:
		staffids.append(staffj.staffId)
	passanger_list = get_passenger_list(journey)
	return render(request, 'car_pool/journey_detail.html', {'journey': journey,
															'staffids': staffids,
															'passenger_list': passanger_list})

# funtions to add a new instace
@login_required(login_url='/login/')
def car_new(request):
	if request.method == "POST":
		form = CarForm(request.POST)
		if form.is_valid():
			car = form.save(commit=False)
			post.save()
			return redirect('car_detail', pk=car.pk)
	else:
		form = CarForm()
	return render(request, 'car_pool/car_edit.html', {'form': form})

@login_required(login_url='/login/')
def school_new(request):
	if request.method == "POST":
		form = SchoolForm(request.POST)
		if form.is_valid():
			school = form.save(commit=False)
			school.save()
			return redirect('school_list')
	else:
		form = SchoolForm()
	return render(request, 'car_pool/school_edit.html', {'form': form})

@login_required(login_url='/login/')
def faculty_new(request):
	if request.method == "POST":
		form = FacultyForm(request.POST)
		if form.is_valid():
			faculty = form.save(commit=False)
			faculty.save()
			return redirect('faculty_list')
	else:
		form = FacultyForm()
	return render(request, 'car_pool/faculty_edit.html', {'form': form})

@login_required(login_url='/login/')
def journey_booked(request, pk):
	journey = get_object_or_404(Journey, pk=pk)
	journey.book_seat(request.user.staff)
	return render(request, 'car_pool/journey_booked.html', {'journey': journey})


def journey_cancel(request, pk):
	journey = get_object_or_404(Journey, pk=pk)
	staffJourney_list = StaffJourney.objects.filter(journeyId=journey)
	for item in staffJourney_list:
		if item.staffId == request.user.staff:
			item.delete()
	return render(request, 'car_pool/journey_cancel.html', {'journey': journey})

#needds changed from faculty to journey
@login_required(login_url='/login/')
def journey_new(request):
	if request.method == "POST":
		form = JourneyForm(request.POST)
		if form.is_valid():
			journey = form.save(commit=False)
			journey.on_create()
			journey.save()
			return redirect('journey_list')
	else:
		user_name = request.user
		staff = Staff.objects.get(user=user_name)
		staffpk = staff.id
		car = Car.objects.get(driver=staffpk)
		user_home = request.user.staff.homeCampus
		origin = user_home
		data = {'car': car, 'origin': origin}
		form = JourneyForm(initial=data)
	return render(request, 'car_pool/journey_edit.html', {'form': form,
														  'title': "New"})


@login_required(login_url='/login/')
def user_new(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			school = School.objects.all()
			campus_list = OriginOptions.objects.all()
			newstaff = Staff.objects.create(user=user, schoolOfWork=school[0],
			                     driver=False, headOfSchool=False,
								 head0fFaculty=False,
								 uniManagement=False,
								 homeCampus=campus_list[0])
			return redirect('staff_edit', pk=newstaff.pk)
	else:
		form = UserForm()
	return render(request, 'car_pool/user_edit.html', {'form': form})

@login_required(login_url='/login/')
def staff_new(request):
	if request.method == "POST":
		form = StaffForm(request.POST)
		if form.is_valid():
			staff = form.save(commit=False)
			staff.save()
			return redirect('staff_list')
	else:
		form = UserForm()
	return render(request, 'car_pool/staff_edit.html', {'form': form})


# functions to edit an instance of an object
@login_required(login_url='/login/')
def car_edit(request, pk):
	post = get_object_or_404(Car, pk=pk)
	if request.method == "POST":
		form = CarForm(request.POST, instance=post)
		if form.is_valid():
			car = form.save(commit=False)
			car.save()
			return redirect(my_info)
	else:
		form = CarForm(instance=post)
	return render(request, 'car_pool/car_edit.html', {'form': form})

@login_required(login_url='/login/')
def school_edit(request, pk):
	post = get_object_or_404(School, pk=pk)
	if request.method == "POST":
		form = SchoolForm(request.POST, instance=post)
		if form.is_valid():
			school = form.save(commit=False)
			school.save()
			return redirect(school_list)
	else:
		form = SchoolForm(instance=post)
	return render(request, 'car_pool/school_edit.html', {'form': form})

@login_required(login_url='/login/')
def faculty_edit(request, pk):
	post = get_object_or_404(Faculty, pk=pk)
	if request.method == "POST":
		form = FacultyForm(request.POST, instance=post)
		if form.is_valid():
			faculty = form.save(commit=False)
			faculty.save()
			return redirect(faculty_list)
	else:
		form = FacultyForm(instance=post)
	return render(request, 'car_pool/faculty_edit.html', {'form': form})

@login_required(login_url='/login/')
def staff_edit(request, pk):
	staff = get_object_or_404(Staff, pk=pk)
	if request.method == "POST":
		form = StaffForm(request.POST, instance=staff)
		if form.is_valid():
			staff = form.save(commit=False)
			staff.save()
			return redirect(staff_list)
	else:
		form = StaffForm(instance=staff)

	return render(request, 'car_pool/staff_edit.html', {'form': form})


# needs changed from facuilty to journey
@login_required(login_url='/login/')
def journey_edit(request, pk):
	journey = get_object_or_404(Journey, pk=pk)
	if request.method == "POST":
		form = JourneyForm(request.POST, instance=journey)
		if form.is_valid():
			journey = form.save(commit=False)
			journey.save()
			return redirect(journey_list)
	else:
		form = JourneyForm(instance=journey)
	return render(request, 'car_pool/journey_edit.html', {'form': form,
															'title': "Edit"
})
