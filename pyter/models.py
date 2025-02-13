from django.db import models


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25)
    
    def __str__(self):
        return self.nome


class Produtos(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Situacoes(models.Model):
    id_situacao = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class Materiais(models.Model):
    id_material = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    preco_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    preco_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome
    

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=30)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class ItensPedido(models.Model):
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='id_pedido', blank=True, null=True)
    id_variacao = models.ForeignKey('VariacoesProdutos', models.DO_NOTHING, db_column='id_variacao', blank=True, null=True)
    quantidade = models.IntegerField()


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    data_pedido = models.DateField()
    data_prazo = models.DateField(blank=True, null=True)
    id_situacao = models.ForeignKey('Situacoes', models.DO_NOTHING, db_column='id_situacao', blank=True, null=True)
    observacao = models.CharField(max_length=100, blank=True, null=True)


class VariacoesProdutos(models.Model):
    id_variacao = models.AutoField(primary_key=True)
    id_produto = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    id_material = models.ForeignKey(Materiais, models.DO_NOTHING, db_column='id_material', blank=True, null=True)
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)
    tamanho = models.CharField(max_length=20, blank=True, null=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)