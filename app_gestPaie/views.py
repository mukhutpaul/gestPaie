from django.shortcuts import render
from app_gestPaie.models.paiement import paiment

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def ffrais(request):
    paiement = paiment.objects.all()
     #paiement = paiment.objects.all().count()

    ctx = {
        "paiement": paiement
        "nbrp": len(paiement)
    }
    return render(request,'frais.html',ctx)

def dash(request):
    
    return render(request,'dashboard.html')

def ppaiement(request):
    
    return render(request,'paiement.html')
