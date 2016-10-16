from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Staff
from .forms import CarForm

def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'car_pool/staff_list.html', {'staff': staff})

def car_list(request):
    car_list = Car.objects.all()
    return render(request, 'car_pool/car_list.html', {'car_list': car_list})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_pool/car_detail.html', {'car': car})

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
