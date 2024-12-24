from django.shortcuts import render, redirect, get_object_or_404
from .models import Etudiant
from django.utils import timezone
def index(request):
    etudiants = Etudiant.objects.all()

    if request.method == 'POST':
        if 'ajouter' in request.POST:
            Etudiant.objects.create(
                nom=request.POST['nom'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                classe_choix=request.POST['classe_choix'],
                date_creation = timezone.now(),

            )
        elif 'modifier' in request.POST:
            etudiant = get_object_or_404(Etudiant, id=request.POST['id'])
            etudiant.nom = request.POST['nom']
            etudiant.email = request.POST['email']
            etudiant.telephone = request.POST['telephone']
            etudiant.classe_choix = request.POST['classe_choix']
            date_creation = timezone.now()            
            etudiant.save()
        elif 'supprimer' in request.POST:
            etudiant = get_object_or_404(Etudiant, id=request.POST['id'])
            etudiant.delete()
        
        return redirect('index')

    return render(request, 'templates/index.html', {'etudiants': etudiants})
