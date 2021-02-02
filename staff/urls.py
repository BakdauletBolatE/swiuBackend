from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:url>',stuffDetailView,name="stuffDetailView"),
] 
 