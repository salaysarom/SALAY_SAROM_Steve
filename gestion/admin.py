from django.contrib import admin
from .models import Patient, Medecin, RendezVous

# Classe Admin pour le modèle Patient
class PatientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date_naissance')
    search_fields = ('nom', 'prenom')
    list_filter = ('date_naissance',)

# Classe Admin pour le modèle Medecin
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('nom', 'specialite')
    search_fields = ('nom', 'specialite')
    list_filter = ('specialite',)

# Classe Admin pour le modèle RendezVous
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('patient', 'medecin', 'date')
    list_filter = ('date',)
    search_fields = ('patient__nom', 'medecin__nom')

# Enregistrer les modèles avec leurs classes admin respectives
admin.site.register(Patient, PatientAdmin)
admin.site.register(Medecin, MedecinAdmin)
admin.site.register(RendezVous, RendezVousAdmin)
