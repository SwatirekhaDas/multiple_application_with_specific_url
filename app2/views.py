from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2first(request):
    return render(request,'app2first.html')

def app2second(request):
    return render(request,'app2second.html')

def response(request):
    return HttpResponse("THIS IS MY APP2 STRING")