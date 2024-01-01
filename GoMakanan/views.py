from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import PembeliGo_Makanan
from .form import PembeliForm



# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def pesanan(request):
    return render(request, 'pesanan.html')

def terimakasih(request):
    return render(request, 'terimakasih.html')

#views model dan form

def vieww(request):
    context={}
    form =PembeliForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] =form
    return render(request, "vieww.html" ,context)

def daftar_vieww(request):
    context={}
    context["dataset"] = PembeliGo_Makanan.objects.all()

    return render(request, "daftar_vieww.html" ,context)