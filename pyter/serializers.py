from rest_framework import serializers
from .models import *

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'


class SituacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacoes
        fields = '__all__'
    

class InstituicoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicoes
        fields = '__all__'


class MateriaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materiais
        fields = '__all__'


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'


class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class VariacoesProdutosSerializer(serializers.ModelSerializer):
    produto = serializers.StringRelatedField()
    categoria = serializers.StringRelatedField()
    material = serializers.StringRelatedField()
    class Meta:
        model = VariacoesProdutos
        fields = '__all__'


class ListaVariacoesSerializer(serializers.ModelSerializer):
    produto = serializers.CharField(source='id_produto')
    categoria = serializers.CharField(source='id_categoria')
    material = serializers.CharField(source='id_material')

    class Meta:
        model = VariacoesProdutos
        fields = '__all__'


class ListaPedidosSerializer(serializers.ModelSerializer):
    situacao = serializers.CharField()
    cliente = serializers.CharField()
    data = serializers.DateField()
    prazo = serializers.DateField()
    instituicao = serializers.CharField(allow_null=True)
    valor = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Pedidos
        fields = ['id_pedido', 'situacao', 'cliente', 'data', 'prazo', 'instituicao', 'valor']
