from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_gestPaie.models.frais import Frais
from app_gestpaie.models.paiement import paiment
from django.shortcuts import redirect

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
 
def ppaiement(request):
    paiement = paiment.objects.all()

     ctx = {
        "paiement": paiement,
        "nbrp": len(paiement)
    }

    return render(request,'paiement.html',ctx)

    def deletepaiement(request,id):

        pm = paiment.objects.get(pk=id)
        pms.delete()
        
        return redirect('/frais/')