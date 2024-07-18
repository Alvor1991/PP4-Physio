from django.contrib import admin
from .models import About, ContactRequest, Testimonial

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'read', 'created_on')
    list_filter = ('read', 'created_on')
    search_fields = ('name', 'email')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """
    Admin interface options for the :model:`testimonial.Testimonial`.
    Allows the management of testimonials, including filtering by active status.
    """
    list_display = ('author', 'text', 'active')
    list_filter = ('active',)
    search_fields = ('author', 'text')

