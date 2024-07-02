from django.contrib import admin
from .models import Appointment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Appointment)
class AppointmentAdmin(SummernoteModelAdmin):
    list_display = ('client', 'date', 'notes')
    search_fields = ['client__username']
    list_filter = ('date',)
    summernote_fields = ('notes',)


