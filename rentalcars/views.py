from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Car, Booking
from .forms import BookingForm, CarForm
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.http import HttpResponse

# def home(request):
#     html_content = "<h1>This will be the car rentals home page!</h1><p>Simple HTML page.</p>"
#     return HttpResponse(html_content)


def home(request):
    cars = Car.objects.all()
    return render(request, 'rentalcars/home.html', {'cars': cars})
    # return render(request, 'rentalcars/home.html')


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'rentalcars/car_details.html', {'car': car})

@login_required
def book_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.user = request.user
            booking.save()
            car.is_available = False
            car.save()
            return redirect('my_bookings')
    else:
        form = BookingForm()
    return render(request, 'rentalcars/book_car.html', {'form': form, 'car': car})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user, is_active=True)
    return render(request, 'rentalcars/my_bookings.html', {'bookings': bookings})

def login_redirect_view(request):  # renamed for clarity
    if request.user.is_staff:
        return redirect('admin_dashboard')
    return redirect('my_bookings')

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    if booking.is_active:
        booking.is_active = False
        booking.save()
        booking.car.is_available = True
        booking.car.save()
    return redirect('my_bookings')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Tha admin STUFF Starts here
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    bookings = Booking.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'rentalcars/adminstuff/admin_dashboard.html', {'bookings': bookings})


@login_required
def add_car(request):
    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = CarForm()

    return render(request, 'rentalcars/adminstuff/add_car.html', {'form': form})


@login_required
def manage_cars(request):
   if not request.user.is_staff:
       return redirect('home')
   cars = Car.objects.all()
   return render(request, 'rentalcars/adminstuff/manage_cars.html', {'cars': cars})

@login_required
def delete_car(request, car_id):
   if not request.user.is_staff:
       return redirect('home')
   car = get_object_or_404(Car, id=car_id)
   car.delete()
   return redirect('manage_cars')

@login_required
def update_car(request, car_id):
   if not request.user.is_staff:
       return redirect('home')
   car = get_object_or_404(Car, id=car_id)
   if request.method == 'POST':
       form = CarForm(request.POST, instance=car)
       if form.is_valid():
           form.save()
           return redirect('manage_cars')
   else:
       form = CarForm(instance=car)
   return render(request, 'rentalcars/adminstuff/update_car.html', {'form': form, 'car': car})
