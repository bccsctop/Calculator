from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.home_page,name='homepage'),
    path('cal_post', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('cal_get',views.)

]