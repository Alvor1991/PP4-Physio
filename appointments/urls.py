from . import views
from django.urls import path

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
]