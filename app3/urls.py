from django.urls import path
from app3.views import *

urlpatterns=[
    path("app3first/",app3first,name='app3first'),
    path("app3second/",app3second,name='app3second'),
    path("response/",response,name='response'),
]