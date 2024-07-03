from . import views
from django.urls import path

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('get_available_time_slots/', views.available_time_slots_view, name='get_available_time_slots'),
]
