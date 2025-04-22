from django.db import models
from django.utils import timezone


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=25)
    
    def __str__(self):
        return self.categoria


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    produto = models.CharField(max_length=50)

    def __str__(self):
        return self.produto


class Situacoes(models.Model):
    id_situacao = models.AutoField(primary_key=True)
    situacao = models.CharField(max_length=25)

    def __str__(self):
        return self.situacao


class Instituicoes(models.Model):
    id_instituicao = models.AutoField(primary_key=True)
    instituicao = models.CharField(max_length=25)

    def __str__(self):
        return self.instituicao


class Materiais(models.Model):
    id_material = models.AutoField(primary_key=True)
    material = models.CharField(max_length=50)
    preco_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preco_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.material
    

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=15)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Enderecos(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, db_column='id_cliente', on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.cidade}"


class Pedidos(models.Model):
    class Modalidades(models.TextChoices):
        PRESENCIAL = 'Presencial', 'Presencial'
        ONLINE = 'Online', 'Online'
    
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, db_column='id_cliente', on_delete=models.DO_NOTHING)
    id_instituicao = models.ForeignKey(Instituicoes, db_column='id_instituicao', on_delete=models.DO_NOTHING, null=True, blank=True)
    modalidade = models.CharField(max_length=20, choices=Modalidades.choices, default=Modalidades.PRESENCIAL)
    data_pedido = models.DateField()
    data_prazo = models.DateField()
    id_situacao = models.ForeignKey(Situacoes, db_column='id_situacao', on_delete=models.DO_NOTHING)
    observacao = models.CharField(max_length=100, blank=True, null=True)
    cod_rastreamento = models.CharField(max_length=50, null=True, blank=True)
    data_envio = models.DateField(null=True, blank=True)
    data_entrega = models.DateField(null=True, blank=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #dado congelado (consistência em consulta futura) - 3FN
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Pagamentos(models.Model):
    class MeiosPagamento(models.TextChoices):
        CAIXA = 'Caixa', 'Caixa'
        PICPAY = 'PicPay', 'PicPay'
        MERCADO_PAGO = 'Mercado Pago', 'Mercado Pago'
        PAGBANK = 'PagBank', 'PagBank'
        SUMUP = 'Sumup', 'Sumup'

    class FormasPagamento(models.TextChoices):
        DINHEIRO = 'Dinheiro', 'Dinheiro'
        PIX = 'Pix', 'Pix'
        CREDITO = 'Crédito', 'Crédito'
        DEBITO = 'Débito', 'Débito'

    id_pagamento = models.AutoField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos', db_column='id_pedido', on_delete=models.DO_NOTHING)
    meio_pagamento = models.CharField(max_length=30, choices=MeiosPagamento.choices)
    forma_pagamento = models.CharField(max_length=20, choices=FormasPagamento.choices)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField(default=timezone.now)
    cod_autorizacao = models.CharField(max_length=50, null=True, blank=True)
    parcelas = models.IntegerField(null=False, blank=False, default=1)


class VariacoesProdutos(models.Model):
    id_variacao = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produtos, db_column='id_produto', on_delete=models.CASCADE)
    id_material = models.ForeignKey(Materiais, db_column='id_material', on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categorias, db_column='id_categoria', on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=20)
    preco = models.DecimalField(max_digits=5, decimal_places=2)


class ItensPedido(models.Model):
    id_pedido = models.ForeignKey(Pedidos, db_column='id_pedido', on_delete=models.CASCADE)
    id_variacao = models.ForeignKey(VariacoesProdutos, db_column='id_variacao', on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    observacao = models.CharField(max_length=200, blank=True, null=True)
    adicionais = models.JSONField(blank=True, null=True)
    descontos = models.JSONField(blank=True, null=True)
    preco_unitario_base = models.DecimalField(max_digits=10, decimal_places=2) #dado congelado (consistência em consulta futura) - 3FN
