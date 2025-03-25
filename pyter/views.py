from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


class SituacoesViewSet(viewsets.ModelViewSet):
    queryset = Situacoes.objects.all()
    serializer_class = SituacoesSerializer


class InstituicoesViewSet(viewsets.ModelViewSet):
    queryset = Instituicoes.objects.all()
    serializer_class = InstituicoesSerializer


class MateriaisViewSet(viewsets.ModelViewSet):
    queryset = Materiais.objects.all()
    serializer_class = MateriaisSerializer


class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


class ItensPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItensPedido.objects.all()
    serializer_class = ItensPedidoSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer


class VariacoesProdutosViewSet(viewsets.ModelViewSet):
    queryset = VariacoesProdutos.objects.all()
    serializer_class = VariacoesProdutosSerializer


class ListaVariacoesDetalhadas(generics.ListAPIView):
    queryset = VariacoesProdutos.objects.select_related().all()
    serializer_class = VariacoesDetalhadasSerializer