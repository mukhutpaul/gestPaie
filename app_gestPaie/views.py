from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_gestPaie.models.frais import Frais

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def ffrais(request):
    frais = Frais.objects.all()
    #frais = Frais.objects.all().count()
    
    ctx = {
        "frais": frais,
        "nbrf": len(frais)
    }
    return render(request,'frais.html',ctx)

def dash(request):
    
    return render(request,'dashboard.html')


def deleteFrais(request,id):
        fr = Frais.objects.get(pk=id)
        fr.delete()
        return HttpResponseRedirect('/frais/')
 
