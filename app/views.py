from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

#DISPLAY THE DATA

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}    
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)
    

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

#INSECTION DATA

def insert_topic(request):
    tn=input('enter topic_name: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',d)


def insert_webpage(request):
    tn=input('enter topic_name: ')
    n=input('enter name: ')
    u=input('enter url: ')
    e=input('enter email: ')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
    NWO.save()
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)



def insert_accessrecord(request):
    pk=int(input('enter webpage pk value: '))
    d=input('enter date: ')
    a=input('enter authors: ')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

