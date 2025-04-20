from rest_framework import serializers
from .models import *
from decimal import Decimal

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


class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = '__all__'


class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedidos
        fields = '__all__'


class PagamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamentos
        fields = '__all__'


class ItensPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'


class VariacoesProdutosSerializer(serializers.ModelSerializer):
    produto = serializers.StringRelatedField()
    categoria = serializers.StringRelatedField()
    material = serializers.StringRelatedField()
    class Meta:
        model = VariacoesProdutos
        fields = '__all__'


class ListaVariacoesSerializer(serializers.ModelSerializer):
    produto = serializers.CharField(source='id_produto.produto')
    categoria = serializers.CharField(source='id_categoria.categoria')
    material = serializers.CharField(source='id_material.material')

    class Meta:
        model = VariacoesProdutos
        fields = ['produto', 'categoria', 'material', 'tamanho', 'preco']


class ListaPedidosSerializer(serializers.ModelSerializer):
    situacao = serializers.CharField()
    cliente = serializers.CharField()
    data = serializers.DateField()
    prazo = serializers.DateField()
    instituicao = serializers.CharField(allow_null=True)
    valor_total = serializers.SerializerMethodField()

    class Meta:
        model = Pedidos
        fields = ['id_pedido', 'situacao', 'cliente', 'data', 'prazo', 'instituicao', 'valor_total']
    
    def get_valor_total(self, obj):
        total = Decimal('0')

        itens = ItensPedido.objects.filter(id_pedido=obj)

        for item in itens:
            subtotal = item.preco_unitario_base * item.quantidade
            adicionais_valor = Decimal('0')
            if item.adicionais:
                for adicional in item.adicionais:
                    valor = Decimal(str(adicional.get('valorAdicional', 0)))
                    adicionais_valor += valor
            subtotal += adicionais_valor * item.quantidade
            total += subtotal
        return total


class PedidoInfoSerializer(serializers.ModelSerializer):
    id_pedido = serializers.IntegerField()
    modalidade = serializers.CharField()
    situacao = serializers.CharField()
    data_envio = serializers.DateField()
    data_entrega = serializers.DateField()
    cod_rastreamento = serializers.CharField()
    nome = serializers.CharField()
    cpf = serializers.CharField()
    telefone = serializers.CharField()
    email = serializers.EmailField()
    data = serializers.DateField()
    prazo = serializers.DateField()
    instituicao = serializers.CharField(allow_null=True)
    endereco = serializers.CharField(allow_null=True)
    

    class Meta:
        model = Pedidos
        fields = ['id_pedido', 'modalidade', 'situacao', 'data', 'prazo', 'data_envio', 'data_entrega', 'cod_rastreamento', 'cpf', 'nome', 'telefone', 'email', 'instituicao', 'endereco']


class PedidoItensSerializer(serializers.ModelSerializer):
    quantidade = serializers.IntegerField()
    produto = serializers.CharField()
    categoria = serializers.CharField()
    material = serializers.CharField()
    tamanho = serializers.CharField()
    observacao = serializers.CharField()
    adicionais = serializers.JSONField()
    preco_unitario_base = serializers.DecimalField(max_digits=10, decimal_places=2)
    valor_total = serializers.SerializerMethodField()

    class Meta:
        model = ItensPedido
        fields = ['quantidade', 'produto', 'categoria', 'material', 'tamanho', 'observacao', 'preco_unitario_base', 'adicionais', 'valor_total']

    def get_valor_total(self, obj):
        adicionais_valor = sum(Decimal(str(adicional.get('valorAdicional', 0))) for adicional in (obj.adicionais or []))
        return obj.valor + adicionais_valor * Decimal(obj.quantidade)