from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatment_list, name='treatments'), 
]