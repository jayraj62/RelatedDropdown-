from django.urls import path
from Dropdownapp import views
urlpatterns = [
    path('', views.index),
]
