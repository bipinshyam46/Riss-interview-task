from django.urls import path
from myapp import views
from .views import *


urlpatterns = [
    path('',views.register,name='register'),
    path('loginuser',views.loginuser,name='login'),
    path('userpage',views.userpage,name='userpage')
    ]