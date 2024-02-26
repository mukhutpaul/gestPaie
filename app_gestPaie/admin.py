from django.contrib import admin
from app_gestPaie.models.paiement import *
from app_gestPaie.models.classe import *
from app_gestPaie.models.frais import *
from app_gestPaie.models.eleve import *

# Register your models here.

admin.site.register(paiment)
admin.site.register(Classe)
admin.site.register(Frais)
admin.site.register(Eleve)
