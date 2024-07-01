from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('<int:id>/', views.appointment_detail, name='appointment_detail'),
]


