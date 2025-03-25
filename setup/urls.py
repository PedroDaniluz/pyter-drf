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
router.register('itenspedido', ItensPedidoViewSet, basename='itenspedido')
router.register('pedidos', PedidosViewSet, basename='pedidos')
router.register('variacoes', VariacoesProdutosViewSet, basename='variacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('<int:produto_id>/variacoes/', ListaVariacoesProduto.as_view(), name='variacoes_produto'),
]
