from operator import le
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormRAM
from . import models

# Create your views here.
def index(request):
    return render(request, 'gestion/index.html')

def ajout1(request):
    return render(request,'gestion/ajout.html')

def ajoutram(request):
    return render(request,'gestion/ajoutram.html')

def show(request):
    return render(request, 'gestion/show.html')

def showram(request):
    queryset = models.RAM.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"gestion/showram.html",{"gestion_ram" : queryset})

def formulaire(request):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid():
            return HttpResponseRedirect("/gestion/traitement")
        else:
            return render(request, 'gestion/ajoutram.html', {'form': form})
    else:
        form = FormRAM()
        return render(request, 'gestion/index.html', {'form': form})

def traitement(request):
    lform = FormRAM(request.POST)
    if lform.is_valid():
        ram = lform.save()
        return render(request,"gestion/index.html",{"Ram" : ram})
    else:
        return render(request,"gestion/ajoutram.html",{"form": lform})


def ajout(request, id):
    if request.method == "POST":
        form = FormRAM(request)
        if form.is_valid(): # validation du formulaire.
            ram = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"Ram" : ram}) #

        else:
            return render(request,"gestion/ajoutram.html",{"form": form})
    else :
        form = FormRAM() # création d'un formulaire vide
        return render(request,"gestion/ajoutram.html",{"form" : form})

def deleteram(request, id):
    id = models.RAM.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/gestion/show/ram")

def updateram(request, id):
    ram = models.RAM.objects.get(pk=id)
    form = FormRAM(ram.dico())
    return render(request, 'gestion/ajoutram.html',{"form":form, "id":id})

def updateramtraitement(request, id):
    lform = FormRAM(request.POST)
    if lform.is_valid():
        ram = lform.save(commit = False)
        ram.id = id
        ram.save()
        return render(request,"gestion/index.html",{"Ram" : ram})
    else:
        return render(request,"gestion/ajoutram.html",{"form": lform, 'id':id})
