from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormRAM
from . import models

# Create your views here.
def index(request):
    return render(request, 'gestion/index.html')

def ajout(request):
    return render(request,'gestion/ajout.html')

def show(request):
    return render(request, 'gestion/show.html')

def showram(request):
    queryset = models.RAM.objects.all()  
    return render(request,"gestion/showram.html",{"Ram " : queryset})

def formulaire(request):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid():
            return HttpResponseRedirect("/gestion/traitement")
        else:
            return render(request, 'gestion/ajout.html', {'form': form})
    else:
        form = FormRAM()
        return render(request, 'gestion/index.html', {'form': form})

def traitement(request):
    lform = FormRAM(request.POST)
    if lform.is_valid():
        ram = lform.save()
        return render(request,"gestion/index.html",{"Ram" : ram})
    else:
        return render(request,"gestion/ajout.html",{"form": lform})


def ajout(request):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid(): # validation du formulaire.
            ram = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"Ram" : ram}) #

        else:
            return render(request,"gestion/ajout.html",{"form": form})
    else :
        form = FormRAM() # création d'un formulaire vide
        return render(request,"gestion/ajout.html",{"form" : form})
