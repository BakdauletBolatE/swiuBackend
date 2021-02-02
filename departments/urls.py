from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:url>',departmentDetailView,name="departmentDetailView"),
    path('edu/<slug:url>',eduProgramDetail,name="eduProgDetailView")
] 
 