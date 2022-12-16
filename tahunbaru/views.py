from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def tahunBaru(request):
    skrng = datetime.datetime.now()
    return render(request, "page/index.html", {
        "thnbru": skrng.month == 1 and skrng.day == 1
    })
