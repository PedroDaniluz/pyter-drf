from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from django.db.models import Sum, F, Value, DecimalField
from django.db.models.functions import Coalesce


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


class ListaVariacoesViewSet(generics.ListAPIView):
    queryset = VariacoesProdutos.objects.select_related().all()
    serializer_class = ListaVariacoesSerializer


class ListaPedidosViewSet(generics.ListAPIView):
    serializer_class = ListaPedidosSerializer

    def get_queryset(self):
        queryset = Pedidos.objects.annotate(
            situacao=F('id_situacao__nome'),
            cliente=F('id_cliente__nome'),
            data=F('data_pedido'),
            prazo=F('data_prazo'),
            instituicao=F('id_instituicao__nome'),
            valor=Coalesce(
                Sum(
                    F('itenspedido__quantidade') * F('itenspedido__id_variacao__preco'),
                    output_field=DecimalField(max_digits=10, decimal_places=2)
                ),
                Value(0.0),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        ).order_by('id_pedido')

        return queryset
