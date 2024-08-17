from django.urls import path
from . import views
from django.views.generic import TemplateView

# Define URL patterns for the home app
urlpatterns = [
    path('', views.home_view, name='home'),
    path(
        'welcome/',
        TemplateView.as_view(template_name='welcome.html'),
        name='welcome'
    ),
]
