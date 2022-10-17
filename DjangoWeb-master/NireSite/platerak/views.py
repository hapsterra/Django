from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Platera, Erosketa


# Create your views here.
def index(request):
    nireplaterak= Platera.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'nireplaterak': nireplaterak,
    }
    return HttpResponse(template.render(context, request))
def erosketak(request):
    nireErosketak = Erosketa.objects.all()
    uni = []
    for x in nireErosketak:
        unia = x.plateraIzena.prezioa * x.kantitatea
        uni.append(unia)
    template = loader.get_template('erosketak.html')

    context = {
        'nireErosketak': nireErosketak,
        'uni': uni,

    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    i = request.POST['izen']
    ing = request.POST['ingrediente']
    al = request.POST['alergeno']
    pr = request.POST['prezio']
    plater = Platera(izena=i, ingredienteak=ing, alergenoak=al, prezioa=pr)
    plater.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  plater = Platera.objects.get(id=id)
  plater.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  nirePlatera = Platera.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'nirePlatera': nirePlatera,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  iz = request.POST['izen']
  ing = request.POST['ingrediente']
  al = request.POST['alergeno']
  pr = request.POST['prezio']
  plater = Platera.objects.get(id=id)
  plater.izena = iz
  plater.ingredienteak = ing
  plater.alergenoak = al
  plater.prezioa = pr
  plater.save()
  return HttpResponseRedirect(reverse('index'))