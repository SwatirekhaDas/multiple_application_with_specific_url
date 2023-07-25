from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app3first(request):
    return render(request,'app3first.html')

def app3second(request):
    return render(request,'app3second.html')

def response(Request):
    return HttpResponse('app3string response')

