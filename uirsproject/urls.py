"""uirsproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from ok.views import base_view, category_view, personal_view, new_employee, new_position, new_category, new_vacation
from django.conf import settings
from django.conf.urls.static import static
from laboratory.views import new_lab_test, new_lab_test_input, RollAuto, LabTests, tests_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_view, name='base'),
    path('newemployee/', new_employee, name='new_employee'),
    path('newcategory/', new_category, name='new_category'),
    path('newvacation/', new_vacation, name='new_vacation'),
    path('test_list/', tests_list, name='test_list'),
    path('newposition/', new_position, name='new_position'),
    path('newlabtest/', new_lab_test, name='new_lab_test'),
    path('labtestsview/', LabTests.as_view(), name='lab_test_view'),
    path('roll-auto/', RollAuto.as_view(), name='roll-auto'),
    path('newlabtestinput/', new_lab_test_input, name='new_lab_test_input'),
    path('category/<slug:category_slug>/', category_view, name='category_detail'),
    path('personal/<slug:personal_slug>', personal_view, name='personal_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)