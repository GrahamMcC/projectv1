from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#functions to get a sub set of journeys

def get_journey_from_id(id):
	current_journey = Journey.objects.get(pk=id)
	return current_journey

def user_equals_driver(staff_object):
	drivers_car = Car.objects.filter(driver=staff_object)
	journey_list = Journey.objects.filter(car=drivers_car)
	return journey_list

def user_equals_passanger(staff_object):
	staffJourneys_list = StaffJourney.objects.filter(staffId=staff_object)
	jobject_list = []
	for staffJourney in staffJourneys_list:
		myjourney = get_journey_from_id(staffJourney.journeyId_id)
	return jobject_list

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
def reports(request):
	return render(request, 'car_pool/reports.html')

@login_required(login_url='/login/')
def my_info(request):
	#get_users_car
	users_car = Car.objects.filter(driver=request.user.staff)
	#get list of journeys where user is driver
	user_is_driver = user_equals_driver(request.user.staff)
	#get list of journeys where user is passanger
	user_is_passanger = user_equals_passanger(request.user.staff)
	return render(request, 'car_pool/my_info.html', {'car_list': users_car,
													'user_is_driver': user_is_driver,
													'user_is_passanger':user_is_passanger})


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
	journey_list = Journey.objects.all()
	my_journey_list = []
	for journey in journey_list:
		if journey.available_seats > 0:
			my_journey_list.append(journey)
	staffjourney = StaffJourney.objects.all()
	staffids = []
	for staffj in staffjourney:
		staffids.append(staffj.staffId)
	return render(request, 'car_pool/journey_list.html',
							{'journey_list': my_journey_list,
							 'staffids': staffids
							})

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
	return render(request, 'car_pool/journey_detail.html', {'journey': journey,
												'staffids': staffids})


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
	return render(request, 'car_pool/journey_booked.html', {'journey': journey})


#needds changed from faculty to journey
@login_required(login_url='/login/')
def journey_new(request):
	if request.method == "POST":
		form = JourneyForm(request.POST)
		if form.is_valid():
			journey = form.save(commit=False)
			journey.save()
			return redirect('journey_list')
	else:
		user_name = request.user
		staff = Staff.objects.get(user=user_name)
		staffpk = staff.id
		car = Car.objects.get(driver=staffpk)
		data = {'car': car}
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
			newstaff = Staff.objects.create(user=user, schoolOfWork=school[0],
			                     driver=False, headOfSchool=False,
								 head0fFaculty=False,
								 uniManagement=False)
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
	return render(request, 'car_pool/school_edit.html', {'form': form})

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
