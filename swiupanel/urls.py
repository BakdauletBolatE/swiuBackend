from django.urls import path
from .views import *
from .widget import addPage, addWidgetType,indexPage,viewPage,getWidgetJson,addWidgetItem


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
    path('searchedu/<str:search>/',searchEdu,name="searchEdu"),
]

urlpatterns += [
    path('page/',indexPage,name="pageIndex"),
    path('page/<str:id>/',viewPage,name="viewPage"),
    path('page/add',addPage,name="addPage"),
]

urlpatterns += [
    # path('activity/',indexPage,name="pageIndex"),
    # path('activity/<str:id>/',activDepAdd,name="activDepAdd"),
    path('activDepAdd/add',activDepAdd,name="activDepAdd"),
    path('activDepList/',activDepList,name="activDepList"),
    path('activityDepCat/add',activDepCatAdd,name="activDepCatAdd")
]

urlpatterns += [
    path('widgettype/add/',addWidgetType,name="addWidgetType"),
    path('getjson-widget/',getWidgetJson,name="getWidgetJson")
]

urlpatterns += [
    path('widgetitem/add',addWidgetItem,name="addWidgetItem")
]