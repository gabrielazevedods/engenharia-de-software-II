from django.shortcuts import render, redirect
from .forms import DisciplinaForm
from .models import Disciplina

# Create your views here.

def disciplina_list(request):
    context = {'disciplina_list':Disciplina.objects.all()}
    return render(request, "disciplina/disciplina_list.html", context)

def disciplina_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = DisciplinaForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados do Tarefa correspondentes à chave primária referente ao id
            disciplina = Disciplina.objects.get(pk = id)
            form = DisciplinaForm(instance = disciplina)
        return render(request, "disciplina/disciplina_form.html", {'form': form})
    else:
        if id == 0: # Operação de inserir uma nova Tarefa
            form = DisciplinaForm(request.POST)
        else: # Operação de atualizar uma Tarefa já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            disciplina = Disciplina.objects.get(pk = id)
            form = DisciplinaForm(request.POST, instance = disciplina)
        if form.is_valid(): 
            form.save()
        return redirect('/disciplina/list')            

def disciplina_delete(request, id):
    disciplina = Disciplina.objects.get(pk = id)
    disciplina.delete()
    return redirect('/disciplina/list')
