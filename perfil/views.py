from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Sum
from .models import Conta, Categoria
from extrato.models import Valor
from .utils import calcula_total, calcula_equilibrio_financeiro
from datetime import datetime


def home(request):
    valores = Valor.objects.filter(data__month = datetime.now().month)
    entradas = valores.filter(tipo = 'E')
    saidas = valores.filter(tipo = 'S')

    total_entradas = calcula_total(entradas, 'extrato')
    total_saidas = calcula_total(saidas, 'extrato')

    contas = Conta.objects.all()

    total_contas = calcula_total(contas, 'extrato')

    percentual_gastos_essenciais, percentual_gastos_nao_essenciais = calcula_equilibrio_financeiro()
    return render(request, 'home.html', {
        'contas': contas, 
        'total_contas': total_contas, 
        'total_entradas': total_entradas, 
        'total_saidas': total_saidas, 
        'percentual_gastos_essenciais': int(percentual_gastos_essenciais), 
        'percentual_gastos_nao_essenciais': int(percentual_gastos_nao_essenciais),
        })


def gerenciar(request):
    contas = Conta.objects.all()
    categorias = Categoria.objects.all()
    total_contas = calcula_total(contas, 'extrato')

    return render(request, 'gerenciar.html', {'contas':contas, 'total_contas': total_contas, 'categorias': categorias})  


def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    extrato = request.POST.get('extrato')
    icone = request.FILES.get('icone')

    if len(apelido.strip()) == 0 or len(extrato.strip()) == 0:
        messages.add_message(request, constants.ERROR, 'Preencha Todos os Campos')
        return redirect('/perfil/gerenciar/')

    conta = Conta(
        apelido=apelido,
        banco=banco,
        tipo=tipo,
        extrato=extrato,
        icone=icone
    )

    conta.save()
    
    messages.add_message(request, constants.SUCCESS, 'Conta cadastrada com sucesso.')
    return redirect('/perfil/gerenciar/')


def deletar_banco(request, id):
    conta = Conta.objects.get(id=id)
    conta.delete()
    
    messages.add_message(request, constants.SUCCESS, 'Conta removida com sucesso!')
    return redirect('/perfil/gerenciar/')


def cadastrar_categoria(request):
    nome = request.POST.get('categoria')
    essencial = bool(request.POST.get('essencial'))
    
    categoria = Categoria(
        categoria=nome,
        essencial=essencial, 
    )

    categoria.save()

    messages.add_message(request, constants.SUCCESS, 'Categoria cadastrada com sucesso.')
    return redirect('/perfil/gerenciar/')


def update_categoria(request, id):
    categoria= Categoria.objects.get(id=id)

    categoria.essencial = not categoria.essencial

    categoria.save()    

    return redirect('/perfil/gerenciar/')


def dashboard(request):
    dados = {}

    categorias = Categoria.objects.all()

    for categoria in categorias:     
        dados[categoria.categoria] = Valor.objects.filter(categoria=categoria).aggregate(Sum('valor'))['valor__sum']

    return render(request, 'dashboard.html', {'labels': list(dados.keys()), 'values': list(dados.values())})
