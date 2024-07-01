from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatments_view, name='treatments'),
]
