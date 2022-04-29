from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormRAM

# Create your views here.
def index(request):
    return render(request, 'gestion/index.html')

def ajout(request):
    return render(request,'gestion/ajout.html')

def formulaire(request):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid():
            return HttpResponseRedirect("/gestion/traitement")
        else:
            return render(request, 'gestion/ajout.html', {'form': form})
    else:
        form = FormRAM()
        return render(request, 'gestion/index', {'form': form})

def traitement(request):
    pForm = FormRAM(request.POST)
    if pForm.is_valid():
        livre = pForm.save()
        return render(request, 'gestion/ram.html' , {'ram' : livre})
    else:
        return render(request, 'gestion/index', {'form': pForm})

def ajout(request):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid(): # validation du formulaire.
            livre = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"livre" : livre}) #

        else:
            return render(request,"gestion/ajout.html",{"form": form})
    else :
        form = FormRAM() # création d'un formulaire vide
        return render(request,"gestion/ajout.html",{"form" : form})
