from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def ais(request):
    return HttpResponse("Hallo Ais")


def leslie(request):
    return HttpResponse("Hallo leslie")


def sapa(request, nama):
    return render(request, "hello/sapa.html", {
      "nama": nama.capitalize()
    })
