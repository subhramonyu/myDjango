from django.urls import path as url
from greetingsapp import views


urlpatterns = [
    url(r'morning',views.goodMorning),
    url(r'evening',views.goodEvening),
]