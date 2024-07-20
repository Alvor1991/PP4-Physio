from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'formatted_date', 'formatted_time', 'treatment', 'notes')
    search_fields = ('user__username', 'treatment')
    list_filter = ('date', 'time', 'treatment')

    def formatted_date(self, obj):
        return obj.date.strftime('%Y-%m-%d')
    formatted_date.short_description = 'Date'

    def formatted_time(self, obj):
        return obj.time.strftime('%H:%M') if obj.time else 'N/A'
    formatted_time.short_description = 'Time'
