from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def goodMorning(request):
    s ='<h2> Hi...!!! ,Good Morning </h2>'
    return HttpResponse(s)

def goodEvening(request):
    s ='<h2> Hi ...!!! ,Good Evening </h2>'
    return HttpResponse(s)
