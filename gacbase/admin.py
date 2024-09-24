from django.contrib import admin
from .models import Cliente, Prestador, Produto,Estoque, Pedido, Pagamentos

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Prestador)
admin.site.register(Produto)
admin.site.register(Estoque)
admin.site.register(Pedido)
admin.site.register(Pagamentos)
