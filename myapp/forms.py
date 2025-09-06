# forms.py
from django import forms
from .models import CarBooking

class CarBookingForm(forms.ModelForm):
    class Meta:
        model = CarBooking
        fields = ['name', 'mobile', 'email', 'pickup', 'trip', 'departure', 'arrival']
