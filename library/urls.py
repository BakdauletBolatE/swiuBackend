from django.urls import path
from .views import *


urlpatterns = [
    path('index/',libindex,name="libindex"),
    path('book/<slug:url>',bookList,name="bookList"),
    path('d/<slug:url>/',bookDetail,name="bookDetail"),
    path('distancelearning/',dlearning,name="dlearning")
]