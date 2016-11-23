from django.shortcuts import render, get_object_or_404, redirect
from .models import Staff, Car, Faculty, School, Journey, StaffJourney
from .forms import CarForm, facultyForm

#functions to login
def log_in(request):
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
        form = schoolForm(request.POST)
        if form.is_valid():
            school = form.save(commit=False)
            post.save()
            return redirect('school_list')
    else:
        form = schoolForm()
    return render(request, 'car_pool/school_edit.html', {'form': form})

def faculty_new(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            faculty = form.save(commit=False)
            post.save()
            return redirect('faculty_list')
        else:
            form = facultyForm()
            return render(request, 'car_pool/faculty_edit.html', {'form': form})

#needds changed from faculty to journey
def journey_new(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            faculty = form.save(commit=False)
            post.save()
            return redirect('faculty_list')
        else:
            form = facultyForm()
            return render(request, 'car_pool/faculty_edit.html', {'form': form})

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
        form = schoolForm(instance=post)
    return render(request, 'car_pool/school_edit.html', {'form': form})

def faculty_edit(request, pk):
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
