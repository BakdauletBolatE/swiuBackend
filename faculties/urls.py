from django.urls import path,include
from .views import *

urlpatterns = [
    path('',facultView,name="facult"),
    path('<slug:url>/',facultDetailView,name="facultDetailView"),
]