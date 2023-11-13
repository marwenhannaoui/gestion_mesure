from django.shortcuts import render, redirect
from .models import Grandeur, Mesure

from .forms import GrandeurForm


def detail(request, id):
    grandeur = Grandeur.objects.get(pk=id)
    return render(request, "grandeurs/detail.html", {"grandeur": grandeur})

def grandeurs_list(request):
    return render(request, "grandeurs/grandeurs_list.html",{"grandeurs": Grandeur.objects.all()})

def new(request):
    if request.method == "POST":
        form = GrandeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = GrandeurForm()
    return render(request, "grandeurs/new.html", {"form": form})


def DeleteGrandeur(request, id):
    grandeur = Grandeur.objects.get(id=id)
    try:
        grandeur.delete()
    except:
        pass
    return redirect('grandeurs')