from django.shortcuts import render


def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sorvete',
        3: 'Sopa de Legumes',
        4: 'Bolo de Chocolate'
    }

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, 'index.html', dados)


def receita(request):
    return render(request, 'receita.html')
