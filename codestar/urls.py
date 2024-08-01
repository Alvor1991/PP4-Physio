from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appointments.views import immediate_logout_view

urlpatterns = [
    path('', include('home.urls')),  
    path('about/', include('about.urls')),
    path('treatments/', include('treatments.urls')),
    path('appointments/', include('appointments.urls')),
    path('accounts/logout/', immediate_logout_view, name='account_logout'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)