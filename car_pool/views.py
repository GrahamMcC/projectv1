from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login

#functions to login
def login(request):
	#https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html
	return render(request, 'car_pool/log_in.html')

#function for forgot password
def forgot_password(request):
	return render(request, 'car_pool/log_in.html')

def admin(request):
	return render(request, 'car_pool/admin.html')

def reports(request):
	return render(request, 'car_pool/reports.html')

#fuctions to return a list of instances
def staff_list(request):
	staff = Staff.objects.all()
	return render(request, 'car_pool/staff_list.html',
						   {'staff': staff})

def car_list(request):
	car_list = Car.objects.all()
	return render(request, 'car_pool/car_list.html',
						   {'car_list': car_list})

def faculty_list(request):
	faculty_list =  Faculty.objects.all()
	for faculty in faculty_list:
		list_of_schools = School.objects.filter(faculty=faculty.pk)
		faculty.list_of_schools = list_of_schools
	return render(request, 'car_pool/faculty_list.html',
						   {'faculty_list': faculty_list})

def school_list(request):
	school_list =  School.objects.all()
	return render(request, 'car_pool/school_list.html',
						   {'school_list': school_list})

def journey_list(request):
	return render(request, 'car_pool/journey_list.html')

# funtions to look at an instance in more detail
def car_detail(request, pk):
	car = get_object_or_404(Car, pk=pk)
	return render(request, 'car_pool/car_detail.html', {'car': car})

def journey_detail(request, pk):
	return render(request, 'car_pool/journey_detail.html')

# funtions to add a new instace
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

#needds changed from faculty to journey
def journey_new(request):
	if request.method == "POST":
		form = JourneyForm(request.POST)
		if form.is_valid():
			journey = form.save(commit=False)
			journey.save()
			return redirect('journey_list')
	else:
		form = JourneyForm()
	return render(request, 'car_pool/journey_edit.html', {'form': form})


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
def car_edit(request, pk):
	post = get_object_or_404(Car, pk=pk)
	if request.method == "POST":
		form = CarForm(request.POST, instance=post)
		if form.is_valid():
			car = form.save(commit=False)
			car.save()
			return redirect('car_detail', pk=car.pk)
	else:
		form = CarForm(instance=post)
	return render(request, 'car_pool/car_edit.html', {'form': form})

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
def journey_edit(request, pk):
	post = get_object_or_404(Faculty, pk=pk)
	if request.method == "POST":
		form = facultyForm(request.POST, instance=post)
		if form.is_valid():
			faculty = form.save(commit=False)
			faculty.save()
			return redirect(faculty_list)
	else:
		form = facultyForm(instance=post)
	return render(request, 'car_pool/faculty_edit.html', {'form': form})
