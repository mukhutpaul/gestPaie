from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def ffrais(request):
    
    return render(request,'frais.html')

def dash(request):
    
    return render(request,'dashboard.html')
