from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pyter.views import *

router = routers.DefaultRouter()
router.register('categorias', CategoriasViewSet, basename='categorias')
router.register('produtos', ProdutosViewSet, basename='produtos')
router.register('situacoes', SituacoesViewSet, basename='situacoes')
router.register('materiais', MateriaisViewSet, basename='materiais')
router.register('instituicoes', InstituicoesViewSet, basename='instituicoes')
router.register('clientes', ClientesViewSet, basename='clientes')
router.register('enderecos', EnderecosViewSet, basename='enderecos')
router.register('pedidos', PedidosViewSet, basename='pedidos')
router.register('pagamentos', PagamentosViewSet, basename='pagamentos')
router.register('itenspedido', ItensPedidoViewSet, basename='itenspedido')
router.register('variacoes', VariacoesProdutosViewSet, basename='variacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('lista-variacoes/', ListaVariacoesViewSet.as_view(), name='lista-variacoes'),
    path('lista-pedidos/', ListaPedidosViewSet.as_view(), name='lista-pedidos'),
    path('pedido-info/<int:id_pedido>/', PedidoInfoViewSet.as_view(), name='pedido-info'),
    path('pedido-itens/<int:id_pedido>/', PedidoItensViewSet.as_view(), name='pedido-itens'),
    path('pedido-pagamentos/<int:id_pedido>/', PedidoPagamentoViewSet.as_view(), name='pedido-pagamentos'),
    path('registrar-pedido/', PedidoCompletoAPIView.as_view(), name='registrar-pedido'),
]
