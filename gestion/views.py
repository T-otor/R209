from operator import le
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FormCPU, FormHDD, FormMarque, FormRAM
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


def ajoutram(request, id):
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


def ajoutcpu(request, id):
    if request.method == "POST":
        form = FormCPU(request)
        if form.is_valid(): # validation du formulaire.
            cpu = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"Cpu" : cpu}) #

        else:
            return render(request,"gestion/ajoutcpu.html",{"form": form})
    else :
        form = FormCPU() # création d'un formulaire vide
        return render(request,"gestion/ajoutcpu.html",{"form" : form})
def traitementcpu(request):
    lform = FormCPU(request.POST)
    if lform.is_valid():
        cpu = lform.save()
        return render(request,"gestion/index.html",{"Cpu" : cpu})
    else:
        return render(request,"gestion/ajoutcpu.html",{"form": lform})
def showcpu(request):
    queryset = models.CPU.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"gestion/showcpu.html",{"gestion_cpu" : queryset})

def updatecpu(request, id):
    cpu = models.CPU.objects.get(pk=id)
    form = FormCPU(cpu.dico())
    return render(request, 'gestion/ajoutcpu.html',{"form":form, "id":id})

def deletecpu(request, id):
    id = models.CPU.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/gestion/show/cpu")

def updatehdd(request, id):
    hdd = models.HDD.objects.get(pk=id)
    form = FormHDD(hdd.dico())
    return render(request, 'gestion/ajouthdd.html',{"form":form, "id":id})

def deletehdd(request, id):
    id = models.HDD.objects.get(pk=id)
    id.delete()
    return HttpResponseRedirect("/gestion/show/hdd")


def showhdd(request):
    queryset = models.HDD.objects.all()  
    print(queryset)
    print(len(queryset))
    return render(request,"gestion/showhdd.html",{"gestion_hdd" : queryset})


def ajouthdd(request, id):
    if request.method == "POST":
        form = FormHDD(request)
        if form.is_valid(): # validation du formulaire.
            hdd = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"Hdd" : hdd}) #

        else:
            return render(request,"gestion/ajouthdd.html",{"form": form})
    else :
        form = FormHDD() # création d'un formulaire vide
        return render(request,"gestion/ajouthdd.html",{"form" : form})

def traitementhdd(request, id):
    lform = FormHDD(request.POST)
    if lform.is_valid():
        hdd = lform.save()
        return render(request,"gestion/index.html",{"Hdd" : hdd})
    else:
        return render(request,"gestion/ajouthdd.html",{"form": lform})


def ajoutemarque(request):
    if request.method == "POST":
        form = FormMarque(request)
        if form.is_valid(): # validation du formulaire.
            marque = form.save() # sauvegarde dans la base
            return render(request,"gestion/affiche.html",{"Marque" : marque}) #

        else:
            return render(request,"gestion/ajoutmarque.html",{"form": form})
    else :
        form = FormMarque() # création d'un formulaire vide
        return render(request,"gestion/ajoutmarque.html",{"form" : form})

def traitementmarque(request):
    lform = FormMarque(request.POST)
    if lform.is_valid():
        marque = lform.save()
        return render(request,"gestion/index.html",{"Marque" : marque})
    else:
        return render(request,"gestion/ajoutmarque.html",{"form": lform})        