from django.db import models


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, null=False, blank=False)
    
    def __str__(self):
        return self.nome


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Situacoes(models.Model):
    id_situacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome


class Instituicoes(models.Model):
    id_instituicao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.nome


class Materiais(models.Model):
    id_material = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    preco_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preco_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=30, null=False, blank=False)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', null=False, blank=False)
    id_instituicao = models.ForeignKey(Instituicoes, models.DO_NOTHING, db_column='id_instituicao', null=True, blank=True)
    data_pedido = models.DateField(null=False, blank=False)
    data_prazo = models.DateField(null=False, blank=False)
    id_situacao = models.ForeignKey(Situacoes, models.DO_NOTHING, db_column='id_situacao', null=False, blank=False)
    observacao = models.CharField(max_length=100, blank=True, null=True)


class VariacoesProdutos(models.Model):
    id_variacao = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='id_produto', null=False, blank=False)
    id_material = models.ForeignKey(Materiais, models.DO_NOTHING, db_column='id_material', null=False, blank=False)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', null=False, blank=False)
    tamanho = models.CharField(max_length=20, null=False, blank=False)
    preco = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)


class ItensPedido(models.Model):
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido', null=False, blank=False)
    id_variacao = models.ForeignKey(VariacoesProdutos, models.DO_NOTHING, db_column='id_variacao', null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
