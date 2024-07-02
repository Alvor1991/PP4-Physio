from . import views
from django.urls import path

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointments'),
    path('<int:id>/', views.appointment_detail, name='appointment_detail'), 
    path('book/', views.book_appointment, name='book_appointment'),
]


