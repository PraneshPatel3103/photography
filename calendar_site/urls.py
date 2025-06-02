from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secure.admin.panel-0369/', admin.site.urls),
    path('', include('calendar_app.urls')),
]
