
from django.contrib import admin
from django.urls import path
from Hostelapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.aboutus),
    path('table/', views.table),
    path('form/', views.form),
]
