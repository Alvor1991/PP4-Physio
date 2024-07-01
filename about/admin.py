from django.contrib import admin
from .models import About, ContactRequest
from django_summernote.admin import SummernoteModelAdmin

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'read', 'created_on')
    list_filter = ('read', 'created_on')
    search_fields = ('name', 'email', 'message')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'email', 'message', 'created_on']
        return []
