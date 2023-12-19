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

