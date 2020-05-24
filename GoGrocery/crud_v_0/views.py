from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio_view(request,*args, **kwargs):
    print(request,args,kwargs)
    return render(request,"base.html",{})

