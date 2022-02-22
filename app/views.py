from django.shortcuts import render, redirect
from app.forms import FilmesForm
from app.models import Filmes

# Create your views here.

def home(request):
    data = {}
    data['db'] = Filmes.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = FilmesForm()
    return render(request, 'form.html', data)

def create(request):
    form = FilmesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    data['form'] = FilmesForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Filmes.objects.get(pk=pk)
    form = FilmesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Filmes.objects.get(pk=pk)
    db.delete()
    return redirect('home')
