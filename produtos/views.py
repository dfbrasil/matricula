from django.shortcuts import render
from .models import Produto

# Create your views here.
def listar_produtos(request):
    produtos = Produto.objects.all()
    context = {
         'lista' : produtos
    }
    return render(request,'produtos/produtos.html',context)

def detalhe_produto(request,id):
    produto = Produto.objects.get(id=id)
    context = {
        'produto':produto
    }
    return render(request,'produtos/detalhe.html',context)