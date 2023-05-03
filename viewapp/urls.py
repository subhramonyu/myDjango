from django.urls import path as url
from viewapp import views



urlpatterns= [
    url(r'time',views.showTIme),
    url(r'date',views.showDate),
]