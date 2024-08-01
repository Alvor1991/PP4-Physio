from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Treatment, FAQ

@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    # Specify which fields should use the Summernote editor
    summernote_fields = ('description', 'services_offered', 'benefits')

    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description', 'benefits', 'services_offered')
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'image')
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
