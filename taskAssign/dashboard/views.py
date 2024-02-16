from django.shortcuts import render
from django.http import JsonResponse
def dashboard(request):
    return render(request,"AdminDashboard.html")

def details(request):
    return render(request,"Details.html")

def task(request):
    return render(request,"Task.html")

def modify(request):
    return render(request,"Modify.html")

def rearrange(request):
    return render(request,"Rearrange.html")
# # Create your views here.
