from django.contrib import admin
from .models import About, ContactRequest


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read', 'created_on')
    list_filter = ('read', 'created_on')
    search_fields = ('name', 'email')