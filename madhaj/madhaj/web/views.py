from django.shortcuts import render
""" import HTTPresponse for print in page """
from django.http import HttpResponseRedirect

from .models import Counseling
from .forms import CounselingForm
# Create your views here.

""" for home page """
def index(request):
    return render(request, 'web/index.html')



""" for counseling farhangian page """
def counselingKafsh(request):
    form = CounselingForm()

    if request.method == 'POST':
        print(request.POST)
        form = CounselingForm(request.POST)
        if form.is_valid():
            form.save()  

    return render(request, 'web/counseling_kafsh.html', {
        "form": form
    })




""" for counseling barnamenavis, servatmand page """
def counselingMadhaj(request):
    form = CounselingForm()

    if request.method == 'POST':
        print(request.POST)
        form = CounselingForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'web/counseling_madhaj.html', {
        "form": form
    })