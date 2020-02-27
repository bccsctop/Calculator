from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='calget'),
    path('admin/', admin.site.urls),
    
]