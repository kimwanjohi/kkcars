from django.urls import path

from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_details'),
    path('car/<int:car_id>/book/', views.book_car, name='book_car'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),

    # admin urlz below
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add-car/', views.add_car, name='add_car'),

    path('manage-cars/', views.manage_cars, name='manage_cars'),
    path('car/<int:car_id>/delete/', views.delete_car, name='delete_car'),
    path('car/<int:car_id>/update/', views.update_car, name='update_car'),
]
