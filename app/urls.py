from django.urls import path

from . import views

urlpatterns = [
    path('lab_3', views.lab_3, name='lab_3'),
    path('lab_4', views.lab_4, name='lab_4'),
    path('lab_5', views.lab_5, name='lab_5'),
]
