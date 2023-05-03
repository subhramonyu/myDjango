from django.shortcuts import render
import time
import datetime
from django.http import HttpResponse 

# Create your views here.

def showTIme(request):
    t = time.time()
    s = '<h2> Current Time is :' +str(t)+'</h2>'
    return HttpResponse(s)

def showDate(request):
    t = datetime.datetime.now()
    s = '<h2> Current Date is :' +str(t)+'</h2>'
    return HttpResponse(s)
