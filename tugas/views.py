from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


class FormTugasBaru(forms.Form):
    tugas = forms.CharField(label="Tugas Baru")
    # prioritas = forms.IntegerField(label="Prioritas", min_value=1, max_value=5)


def tahunApp(request):
    if "kerja" not in request.session:
        request.session["kerja"] = []
    return render(request, "tugas/index.html", {"tugas": request.session["kerja"]})


def tmbh(request):
    if request.method == "POST":
        form = FormTugasBaru(request.POST)
        if form.is_valid():
            tugas = form.cleaned_data["tugas"]
            request.session["kerja"] += [tugas]
            return HttpResponseRedirect(reverse("tahunApp"))
        else:
            return render(request, "tugas/tmbh.html", {"form": form})

    return render(request, "tugas/tmbh.html", {"form": FormTugasBaru()})
