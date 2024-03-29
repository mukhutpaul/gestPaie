from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app_gestPaie.models.frais import Frais
from app_gestPaie.models.paiement import paiment
from django.shortcuts import redirect
from datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template

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

def modifierFrais(request,id):
      f = Frais.objects.get(pk=id)
      
      ctx= {
          'f':f
      }
      return render(request,'modifierFrais.html',ctx)
  
  
def updateFrais(request,id):
      f = Frais.objects.get(pk = id)
      lib = request.POST["libfrais"]
              
      f.libelle  = lib
      
      #print(f.intfrais,f.montant,f.codefrais)
      f.save()
      return HttpResponseRedirect('/frais/')
  

def rapportFrais(request):
    template_path = 'rapport/rapportFrais.html'
   
    fs = Frais.objects.all()
    #pf = paiement.objects.all().group_by('eleve')
    #pf = paiement.objects.aggregate(Sum('montant'))
 

    ctx ={
        'fr': fs ,
        'compte' : len(fs),
        'date' : datetime.now(),
    }
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(ctx)
	
    import sys
    sys.setrecursionlimit(2500)

    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>'+ html +'</pre>')
    
    return response