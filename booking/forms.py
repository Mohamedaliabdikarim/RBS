from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['number_of_people', 'date', 'start_time', 'end_time', 'name', 'email']
