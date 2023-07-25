from django.urls import path
from app2.views import *

urlpatterns=[
    path("app2first/",app2first,name='app2first'),
    path("app2second/",app2second,name='app2second'),
    path("response/",response,name='response'),
]