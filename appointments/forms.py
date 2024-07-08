from django import forms
from .models import Appointment
from .views import get_available_time_slots

class AppointmentForm(forms.ModelForm):
    time_slot = forms.ChoiceField(choices=[], required=True, label="Time Slot")

    class Meta:
        model = Appointment
        fields = ['client_name', 'client_email', 'date', 'time_slot', 'notes']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if 'date' in self.data:
            try:
                date = self.data.get('date')
                available_slots = get_available_time_slots(date)
                self.fields['time_slot'].choices = [(slot, slot) for slot in available_slots]
            except (ValueError, TypeError):
                self.fields['time_slot'].choices = []
        else:
            self.fields['time_slot'].choices = []


