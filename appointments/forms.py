from django import forms
from .models import Appointment
from .utils import get_available_time_slots
from datetime import datetime, date


class DateInput(forms.DateInput):
    """
    Custom DateInput widget to include HTML5 date picker & set a minimum date.
    """
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        # Set minimum date to today to prevent past dates from being selected
        kwargs['attrs'] = {
            'min': date.today().strftime('%Y-%m-%d')
        }
        super().__init__(*args, **kwargs)


class AppointmentForm(forms.ModelForm):
    """
    Form for creating or updating an appointment.
    Includes fields for date, time slot, and treatment.
    """
    date = forms.DateField(widget=DateInput)
    time_slot = forms.ChoiceField(
        choices=[], required=True, label="Time Slot"
    )

    class Meta:
        model = Appointment
        fields = ['date', 'time_slot', 'treatment']  # 'notes' field removed

    def __init__(self, *args, **kwargs):
        """
        Initialize the form. If a date is provided, fetch available time slots.
        Populate the time_slot choices dynamically based on the selected date.
        """
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if 'date' in self.data:
            try:
                date = self.data.get('date')
                available_slots = get_available_time_slots(date)
                self.fields['time_slot'].choices = [
                    (slot, slot) for slot in available_slots
                ]
            except (ValueError, TypeError):
                self.fields['time_slot'].choices = []
        elif self.instance and self.instance.pk:
            # If the form is being used to update an existing appointment
            date = self.instance.date
            available_slots = get_available_time_slots(date)
            self.fields['time_slot'].choices = [
                (slot, slot) for slot in available_slots
            ]
            self.fields['time_slot'].initial = self.instance.time.strftime(
                '%H:%M'
            )
        else:
            self.fields['time_slot'].choices = []

    def save(self, commit=True):
        """
        Save the form, ensuring time slot is saved correctly as a time object.
        """
        appointment = super().save(commit=False)
        appointment.time = datetime.strptime(
            self.cleaned_data['time_slot'], '%H:%M'
        ).time()
        if commit:
            appointment.save()
        return appointment
