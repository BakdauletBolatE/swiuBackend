from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name="swiuindex"),
    path('stafflist/',staffListView,name='staffListView'),
    path('edulist/',eduProListView,name='eduProListView'),
    path('edu/',addEdu,name="addEdu"),
    path('getd/<str:fac>',getDepartments),
    path('staff/',addStaff,name="addStaff"),
    path('staff/edit/<str:url>/',editStaff,name="editStaff"),
    path('get-facult-json/<str:cat>',getFacultStaff),
    path('get-op-json/<str:op>',getOpJson),
    path('searchedu/<str:search>/',searchEdu,name="searchEdu")
]