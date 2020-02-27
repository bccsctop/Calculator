from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.index, name='calget'),
    path('admin/', admin.site.urls),
    path('removehistory/<str:id>', views.remove_history,name='removehistory'),
    path('removeallhistory/',views.remove_all_history,name='removeallhistory')
    
]