from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment, FAQ

@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    # Specify which fields should use the Summernote editor
    summernote_fields = ('description', 'services_offered', 'benefits')

    # Include button_text in the list_display to show it in the admin list view
    list_display = ('name', 'price', 'description', 'button_text')

    # Add button_text to the search fields for search functionality
    search_fields = ('name', 'description', 'benefits', 'services_offered', 'button_text')

    # Add button_text to the fieldsets for editing in the admin form
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'image', 'button_text')  # Include button_text here
        }),
        ('Details', {
            'fields': ('description', 'services_offered', 'benefits'),
            'classes': ('collapse',)  # Optional: Collapse the section for better navigation
        }),
    )

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question', 'answer')