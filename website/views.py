from django.shortcuts import render
from grandeurs.models import Grandeur

def homeView (req):
    context={'grandeurs': Grandeur.objects.all()}

    return render(req,"website/home.html",context=context)
