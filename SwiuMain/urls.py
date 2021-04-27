"""SwiuMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index,aboutUs,pageView,opView,accreditation,enrolleView,toTheStudentsView

from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/',include('django.conf.urls.i18n')),
    path('swiu-panel/',include('swiupanel.urls')),
    path('page-const/',include('page.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 




urlpatterns += i18n_patterns(
    path('',index,name="index"),
    path('about-university',aboutUs,name="aboutU"),
    path('thebestop/',opView,name="opView"),
    path('accreditation/',accreditation,name="accreditation"),
    path('to-the-students/',toTheStudentsView,name="toTheStudents"),
    path('enrolle/',enrolleView,name="enrolle"),
    path('facult/',include('faculties.urls')),
    path('departments/',include('departments.urls')),
    path('stuff/',include('staff.urls')),
    path('creative/',include('news.urls')),
    path('<slug:url>/',pageView,name="pageView"),
    path('library/',include('library.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


