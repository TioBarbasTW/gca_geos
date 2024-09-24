from django.db import models

# Create your models here.

class Cliente(models.Model):
    codCliente = models.CharField(primary_key=True, max_length=11)
    nomeCliente = models.CharField(max_length=30)
    telefoneCliente = models.CharField(max_length=12)

    def __str__(self):
        return self.nomeCliente

class Prestador(models.Model):
    status = {
        'aberto' : 'Aberto',
        'fechado' : 'Fechado'
    }
    codPrestador = models.CharField(primary_key=True,max_length=3)
    statusPrestador = models.BooleanField(default=False, choices=status)
    codCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        txtPrestador = '{0} - {1}'
        return txtPrestador.format(self.codCliente, self.statusPrestador)
            

    
class Produto(models.Model):
    codProduto = models.CharField(primary_key=True, max_length=8)
    descProduto = models.CharField(max_length=30)
    precoUnitarioProduto = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.descProduto
    
class Estoque(models.Model):
    codProduto = models.CharField(primary_key=True, max_length=8)
    estoqueProduto = models.IntegerField(default=0)
    unidadeProduto = models.CharField(default='UND',max_length=3)

    def __str__(self):
        txt = '{0} - {1}{2}'
        self.estProduto = str(self.estoqueProduto)
        return txt.format(self.codProduto,self.estProduto,self.unidadeProduto)
    
class Pedido(models.Model):
    codPedido = models.CharField(primary_key=True, max_length=4)
    codProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    codPrestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    qtdProduto = models.IntegerField(default=0)
    valorConsumido = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    estadoPedido = models.BooleanField(default=False)

    def __str__(self):
        txtPedido = '{0} - {1} - {2}'
        return txtPedido.format(self.codPedido, self.codProduto, self.valorConsumido)
    
class Pagamentos(models.Model):
    formPag = {
        'debito': 'Debito',
        'credito': 'Credito',
        'pix': 'PIX',
        'dinheiro': 'Dinheiro',
        'promo': 'Promocao',
        'pdp': 'PDP',

    }
    codPagamento = models.CharField(primary_key=True, max_length=6)
    codPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    formaPagamento = models.CharField(max_length=10, choices=formPag)
    totalPagamento = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    descontoPagamento = models.DecimalField(default=0, max_digits=6, decimal_places=2)    
    valorPagamento = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        txtPagamento = '{0} - {1} - {2}'
        return txtPagamento.format(self.codPagamento, self.valorPagamento, self.formaPagamento)

