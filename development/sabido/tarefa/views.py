from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa
from django.http import HttpResponse
from django.views.decorators.http import require_safe, require_http_methods, require_GET, require_POST

# Create your views here.

@require_safe
def tarefa_list(request):
    context = {'tarefa_list':Tarefa.objects.all()}
    return HttpResponse(render(request, "tarefa/tarefa_list.html", context))

@require_http_methods(["GET", "POST", "PUT", "PATCH"])
def tarefa_form(request, id = 0):
    if request.method == "GET":
        if id == 0:  # Se o id passado for 0 (Default), então exibirá um formulário em branco para ser utilizado em uma operação de insert
            form = TarefaForm()
        else: # Se o id passado for diferente de 0, exibirá um formulário preenchido com os dados das tarefas correspondentes à chave primária referente ao id
            tarefa = Tarefa.objects.get(pk = id)
            form = TarefaForm(instance = tarefa)
        return HttpResponse(render(request, "tarefa/tarefa_form.html", {'form': form}))
    else:
        if id == 0: # Operação de inserir um nova tarefa
            form = TarefaForm(request.POST)
        else: # Operação de atualizar uma tarefa já existente com a chave primária referente ao id com os dados passados pelo formulário na requisição POST
            tarefa = Tarefa.objects.get(pk = id)
            form = TarefaForm(request.POST, instance = tarefa)
        if form.is_valid(): 
            form.save()
        return redirect('/tarefa/list')            

def tarefa_delete(request, id):
    if request.method == "POST":
        tarefa = Tarefa.objects.get(pk = id)
        tarefa.delete()
        return redirect('/tarefa/list')


