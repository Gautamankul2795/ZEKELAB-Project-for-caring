# it is created by me
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='hompage'),
    path('caretaker/', views.caretaker, name='Tacker'),
    path('careneeder/', views.careneeder, name='Needers'),
    path('contact/', views.contact, name='contect'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('search/', views.search, name='search')
]
