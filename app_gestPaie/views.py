from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_gestPaie.models.frais import Frais
from app_gestPaie.models.paiement import paiment
from django.shortcuts import redirect

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def ajouterFrais(request):
    
    return render(request,'ajouterFrais.html')

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
        pm.delete()
        
        return redirect('/paikement/')
    
    

def addfrais(request):
    message = None
    if request.method == 'POST':
        codefrais = request.POST["codefrais"]
        libfrais = request.POST["libfrais"]
            
        rs_frais = Frais.objects.filter(codeFrais=codefrais)

        if len(rs_frais)>0:
            message ="Ce code frais existe"    
        else:
            frai = Frais(
                  
                  codeFrais = codefrais,
                  libelle = libfrais,
            )  
          
            frai.save()
            message ="frais enregistré avec succès"
            
    ctx ={
        'message':message
    }
    return render(request,'AjouterFrais.html',ctx)