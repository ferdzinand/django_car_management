# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Car
# from .forms import CarForm
# from django.core.paginator import Paginator
# from django.db.models import F
# from django.http import JsonResponse, HttpRequest,HttpResponse
# from django.template.loader import render_to_string
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db import connection
# import sqlite3


# Car_List
def car_list(request):
    
    cars = Car.objects.all()
    colors = Car.objects.order_by().values_list('color', flat=True).distinct()
    selected_color = request.GET.get('color','')
    if selected_color:
        cars = cars.filter(color=selected_color)
    cars = cars.order_by('position', 'id')
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    cars = paginator.get_page(page_number)
    return render(request, 'car_list.html', {'cars': cars, 'colors': colors, 'selected_color': selected_color})

# basic crud

# READ - Car_detail / Display Car details
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'car_detail.html', {'car': car})

# CREATE
def car_addnew(request):
    return redirect(car_edit)

def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_list', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'car_edit.html', {'form': form})

# EDIT/UPDATE
def car_edit(request, pk):
    if request.method == "POST":
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm(instance=car)
    return render(request, 'car_edit.html', {'form': form})



# DELETE
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car_list')

# FUNCTIONS

