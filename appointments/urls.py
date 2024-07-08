from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('get_time_slots/', views.get_time_slots, name='get_time_slots'),
]
