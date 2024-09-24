from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('criarPedido/<str:n>', views.criarPedido, name='criarPedido'),
    path('pedido/', views.pedido, name='pedido')
]