from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin.console@369/', admin.site.urls),
    path('', include('calendar_app.urls')),
]
