from django import forms
from .models import Booking
from .models import Car


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['driving_license', 'start_time', 'duration_hours']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class CarForm(forms.ModelForm):
    image = forms.URLField(required=False)

    class Meta:
        model = Car
        fields = ['name', 'model', 'year', 'charges_per_day', 'description', 'image']
