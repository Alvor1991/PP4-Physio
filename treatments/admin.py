from django.contrib import admin
from .models import Treatment, FAQ

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    # Only include fields that exist in the Treatment model
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