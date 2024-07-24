from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('get_time_slots/', views.get_time_slots, name='get_time_slots'),
    path('my_appointments/', views.user_appointments, name='user_appointments'),
]
