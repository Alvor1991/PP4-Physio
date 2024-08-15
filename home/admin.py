from django.contrib import admin
from .models import ClientTestimonial


# Register the ClientTestimonial model
@admin.register(ClientTestimonial)
class ClientTestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'active', 'date_added')
    list_filter = ('active',)
    search_fields = ('client_name', 'testimonial_text')
