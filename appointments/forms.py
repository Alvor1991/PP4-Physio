from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'notes', 'client_name', 'client_email']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
