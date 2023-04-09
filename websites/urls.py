from django.contrib import admin
from django.urls import path,include

from websites import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout')
]