from django.urls import path
from .views import PageDetailView,PageListView,addWidget,orderedPages,orderedWidgets

urlpatterns = [
    path('list-view/<int:pk>/',PageListView.as_view(),name="pageListView"),
    path('page-detail/<int:pk>/',PageDetailView.as_view(),name="pageDetailView"),
    path('add-widget/<int:pk>/',addWidget,name="addWidget"),
    path('ordered-pages/',orderedPages),
    path('ordered-widgets/',orderedWidgets)
]