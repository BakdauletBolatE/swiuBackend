from django.urls import path
from .views import *

urlpatterns = [
    path('list-view/<int:pk>/',PageListView.as_view(),name="pageListView"),
    path('page-detail/<int:pk>/',PageDetailView.as_view(),name="pageDetailView"),
    path('add-widget/<int:pk>/',addWidget,name="addWidget"),
    path('ordered-pages/',orderedPages),
    path('ordered-widgets/',orderedWidgets),
    path('widget-text-update/<int:pk>',WidgetTextUpdateView.as_view(),name="widgetTextUpdate"),
    path('page-create',PageCreateView.as_view(),name="PageCreateView"),
    path('page-category-create',PageCategoryCreateView.as_view(),name="PageCategoryCreateView"),
    path('page-update/<int:pk>',PageUpdateView.as_view(),name="PageUpdateView"),
    path('page-delete/<int:cat_id>/<int:pk>',PageDeleteView.as_view(),name="PageDeleteView")
]