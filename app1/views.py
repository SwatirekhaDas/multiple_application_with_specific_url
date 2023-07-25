from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1first(request):
    return render(request,'app1first.html')

def app1second(request):
    return render(request,'app1second.html')

def response(request):
    return HttpResponse("THIS IS MY APP1 STRING")