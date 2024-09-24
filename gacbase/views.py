from django.shortcuts import render, redirect
from .models import Cliente, Prestador, Produto, Estoque, Pedido, Pagamentos

# Create your views here.
def home(request):
    infoCliente = Cliente.objects.all()
    infoPrestador = Prestador.objects.all()
    infoProduto = Produto.objects.all()
    infoEstoque = Estoque.objects.all()
    infoPedido = Pedido.objects.all()
    infoPagamento = Pagamentos.objects.all()
    total=15
    chave = []
    for ch in range(total):
        chave.append(ch+1)
    
    return render(request,'clientes.html', {
        'cliente': infoCliente,
        'prestador': infoPrestador,
        'produto': infoProduto,
        'estoque': infoEstoque,
        'pedido': infoPedido,
        'pagamento': infoPagamento,
        'chave':chave
    })

def criarPedido(request, n):
    if request.method == 'GET':
        serv = n
        return render(request, 'criarPedido.html', {
            'serv':serv
        })
    else:
        print('no hice nada')

def pedido(request):
    print(request.POST)
    print('estou aqui')
    return redirect('home')
