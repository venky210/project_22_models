"""
URL configuration for project_22 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display_topic/',display_topic,name='display_topic'),
    path('display_webpage/',display_webpage,name='display_webpage'),
    path('display_accessrecord/',display_accessrecord,name='display_accessrecord'),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_accessrecord/',insert_accessrecord,name='insert_accessrecord'),
    path('ascending_topic/',ascending_topic,name='ascending_topic'),
    path('descending_topic/',descending_topic,name='descending_topic'),
    path('length_topic/',length_topic,name='length_topic'),
    path('ascending_webpage/',ascending_webpage,name='ascending_webpage'),
    path('descending_webpage/',descending_webpage,name='descending_webpage'),
    path('lengthascending_webpage/',lengthascending_webpage,name='lengthascending_webpage'),
    path('lengthdescending_webpage/',lengthdescending_webpage,name='lengthdescending_webpage'),
    path('ascending_accessrecord/',ascending_accessrecord,name='ascending_accessrecord'),
    path('descending_accessrecord/',descending_accessrecord,name='descending_accessrecord'),
    path('lengthascending_accessrecord/',lengthascending_accessrecord,name='lengthascending_accessrecord'),
    path('lengthdescending_accessrecord/',lengthdescending_accessrecord,name='lengthdescending_accessrecord'),
    path('fieldlookup_gt/',fieldlookup_gt,name='fieldlookup_gt'),
    path('fieldlookup_gte/',fieldlookup_gte,name='fieldlookup_gte'),
    path('fieldlookup_lt/',fieldlookup_lt,name='fieldlookup_lt'),
    path('fieldlookup_lte/',fieldlookup_lte,name='fieldlookup_lte'),
    path('fieldlookup_startswith/',fieldlookup_startswith,name='fieldlookup_startswith'),
    path('fieldlookup_endswith/',fieldlookup_endswith,name='fieldlookup_endswith'),
    path('fieldlookup_contains/',fieldlookup_contains,name='fieldlookup_contains'),
    path('fieldlookup_in/',fieldlookup_in,name='fieldlookup_in'),
    path('fieldlookup_regex/',fieldlookup_regex,name='fieldlookup_regex'),
    path('fieldlookup_year/',fieldlookup_year,name='fieldlookup_year'),
    path('fieldlookup_month/',fieldlookup_month,name='fieldlookup_month'),
    path('fieldlookup_day/',fieldlookup_day,name='fieldlookup_day'),
    path('Qobject_and/',Qobject_and,name='Qobject_and'),
    path('and_operation/',and_operation,name='and_operation'),
    path('Qobject_or/',Qobject_or,name='Qobject_or'),
    path('update_webpage/',update_webpage,name='update_webpage'),
]
    
    
