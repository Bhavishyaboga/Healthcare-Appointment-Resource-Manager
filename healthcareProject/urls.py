
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
    # path('Login/', views.Login, name='Login'),
    # Add more paths as 
]