from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

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
    da=input('enter date')
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

#ORDER DATA


def ascending_topic(request):
    QLTO=Topic.objects.all().order_by('topic_name')
    d={'topic':QLTO}   
    return render(request,'display_topic.html',d)


def descending_topic(request):
    QLTO=Topic.objects.all().order_by('-topic_name')
    d={'topic':QLTO}   
    return render(request,'display_topic.html',d)


def length_topic(request):
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    d={'topic':QLTO}   
    return render(request,'display_topic.html',d)

def descendinglength_topic(request):
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    d={'topic':QLTO}   
    return render(request,'display_topic.html',d)


def ascending_webpage(request):
    QLWO=Webpage.objects.all().order_by('name')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def descending_webpage(request):
    QLWO=Webpage.objects.all().order_by('-name')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def lengthascending_webpage(request):
    QLWO=Webpage.objects.all().order_by(Length('name'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def lengthdescending_webpage(request):
    QLWO=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)
  

def ascending_accessrecord(request):
    QLAO=AccessRecord.objects.all().order_by('name')
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

def descending_accessrecord(request):
    QLAO=AccessRecord.objects.all().order_by('-name')
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

def lengthascending_accessrecord(request):
    QLAO=AccessRecord.objects.all().order_by(Length('name'))
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

def lengthdescending_accessrecord(request):
    QLAO=AccessRecord.objects.all().order_by(Length('name').desc())
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)


#FILEDLOOKUPS

def fieldlookup_gt(request):
    QLWO=Webpage.objects.filter(pk__gt=3)
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def fieldlookup_gte(request):
    QLWO=Webpage.objects.filter(pk__gte=3)
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def fieldlookup_lt(request):
    QLWO=Webpage.objects.filter(pk__lt=3)
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_lt(request):
    QLWO=Webpage.objects.filter(pk__lt=3)
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_lte(request):
    QLWO=Webpage.objects.filter(pk__lte=3)
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_startswith(request):
    QLWO=Webpage.objects.filter(name__startswith='r')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_endswith(request):
    QLWO=Webpage.objects.filter(name__endswith='t')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_contains(request):
    QLWO=Webpage.objects.filter(name__contains='r')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def fieldlookup_in(request):
    QLWO=Webpage.objects.filter(name__in=('virat','dhoni','roith'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def fieldlookup_regex(request):
    QLWO=Webpage.objects.filter(name__regex='\w+h$')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def fieldlookup_year(request):
    QLAO=AccessRecord.objects.filter(date__year='2006')
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

def fieldlookup_month(request):
    QLAO=AccessRecord.objects.filter(date__month='06')
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

def fieldlookup_day(request):
    QLAO=AccessRecord.objects.filter(date__day='16')
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)

#IMPORT Q OBJECTS

def Qobject_and(request):
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') & Q(name__startswith='v'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)

def and_operation(request):
    QLWO=Webpage.objects.filter(topic_name='cricket',name__startswith='d')
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def Qobject_or(request):
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(name__startswith='v'))
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)



#update

def update_webpage(request):
    #Webpage,object.filter(url__contains='venkatesh').update(name='venkatesh')
    #Webpage,object.filter(topic_name='cricket').update(name='virat')
    #Webpage.objects.filter(url__contains='venkatesh').update(topic_name='football')
    #VO=Topic.objects.get_or_create(topic_name='volleyball')[0]
    #VO.save()
    #Webpage.objects.update_or_create(name='venkat',defaults={'topic_name':VO})
    #Webpage.objects.update_or_create(topic_name= 'volleyball',defaults={'name':'venkat'})
   
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)
    





