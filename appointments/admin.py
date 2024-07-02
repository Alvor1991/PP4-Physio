from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'date', 'notes')
    search_fields = ('client_name', 'client_email')
    list_filter = ('date',)


