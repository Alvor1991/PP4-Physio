from django import forms
from .models import Appointment
from .utils import get_available_time_slots
from datetime import datetime, date

class DateInput(forms.DateInput):
    """
    Custom DateInput widget to include HTML5 date picker and set a minimum date (today).
    """
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        # Set the minimum date to today to prevent past dates from being selected
        kwargs['attrs'] = {'min': date.today().strftime('%Y-%m-%d')}
        super().__init__(*args, **kwargs)

class AppointmentForm(forms.ModelForm):
    """
    Form for creating or updating an appointment.
    Includes fields for date, time slot, treatment, and notes.
    """
    date = forms.DateField(widget=DateInput)  # Date field with a custom date picker widget
    time_slot = forms.ChoiceField(choices=[], required=True, label="Time Slot")  # Time slot field populated dynamically
    notes = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please describe your issue'}), required=False)  # Optional notes field with a placeholder

    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'treatment', 'notes']  # Specifies the fields to include in the form

    def __init__(self, *args, **kwargs):
        """
        Initialize the form. If a date is provided, fetch available time slots.
        Populate the time_slot choices dynamically based on the selected date.
        """
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if 'date' in self.data:
            try:
                date = self.data.get('date')
                available_slots = get_available_time_slots(date)  # Fetch available time slots for the selected date
                self.fields['time_slot'].choices = [(slot, slot) for slot in available_slots]  # Populate time_slot choices
            except (ValueError, TypeError):
                self.fields['time_slot'].choices = []  # If date is invalid, set an empty choice list
        elif self.instance and self.instance.pk:
            # If the form is being used to update an existing appointment
            date = self.instance.date
            available_slots = get_available_time_slots(date)
            self.fields['time_slot'].choices = [(slot, slot) for slot in available_slots]
            self.fields['time_slot'].initial = self.instance.time.strftime('%H:%M')  # Set the initial value to the existing time slot
        else:
            self.fields['time_slot'].choices = []  # Set an empty choice list if no date is provided

    def save(self, commit=True):
        """
        Save the form, ensuring the time slot is saved correctly as a time object.
        """
        appointment = super().save(commit=False)
        appointment.time = datetime.strptime(self.cleaned_data['time_slot'], '%H:%M').time()  # Convert selected time slot to a time object
        if commit:
            appointment.save()  # Save the appointment if commit is True
        return appointment