from django.shortcuts import render

# Create your views here.


def Identification(request):
    return render(request,"Identification/login.html")