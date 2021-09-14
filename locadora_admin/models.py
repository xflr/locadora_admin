from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.db.models import Q, Count

# Create your models here.

class Genero(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=200)

class Midia(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=200)

class Cat_Preco(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=200)
   valor = models.DecimalField(max_digits=15, decimal_places=2)

class Inventario(models.Model):
   id = models.AutoField(primary_key=True)
   titulo = models.CharField(max_length=200)
   barcode = models.CharField(max_length=200)
   genero = models.ForeignKey(Genero, on_delete=models.DO_NOTHING)
   class_indicativa = models.IntegerField()
   total_estoque = models.IntegerField()
   total_disponivel = models.IntegerField()
   midia = models.ForeignKey(Midia, on_delete=models.DO_NOTHING)
   max_dias = models.IntegerField()
   cat_preco = models.ForeignKey(Cat_Preco, on_delete=models.DO_NOTHING)
   preco_venda = models.DecimalField(max_digits=15, decimal_places=2)

class Clientes(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=200)
   nascimento = models.DateField()
   endereco = models.CharField(max_length=200)
   cep = models.CharField(max_length=9)
   telefone = models.CharField(max_length=20)
   email = models.CharField(max_length=200)
   cpf = models.CharField(max_length=11)
   fator_multa = models.IntegerField()
   pontos_fidelidade = models.IntegerField()

class Usuarios(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=200)
   nascimento = models.DateField()
   endereco = models.CharField(max_length=200)
   cep = models.CharField(max_length=9)
   telefone = models.CharField(max_length=20)
   email = models.CharField(max_length=200)
   cpf = models.CharField(max_length=11)
   isadmin = models.BooleanField()
   login = models.CharField(max_length=200)
   senha = models.CharField(max_length=200)

class Pedidos(models.Model):
   id = models.AutoField(primary_key=True)
   cliente = models.ForeignKey(Clientes, on_delete=models.DO_NOTHING)
   usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
   data_abertura = models.DateField()
   data_prev_fechamento = models.DateField()
   data_fechamento = models.DateField(null=True)
   valor_previsto = models.DecimalField(max_digits=15, decimal_places=2)
   valor_multa = models.DecimalField(max_digits=15, decimal_places=2, null=True)
   valor_final = models.DecimalField(max_digits=15, decimal_places=2, null=True)
   observacoes = models.CharField(max_length=300, null=True)
   quant_itens_pedido = lambda self: self.itens_pedido_set.count()
   pago = models.BooleanField()
   compra = models.BooleanField()
   status = models.BooleanField()

class Itens_Pedido(models.Model):
  pedido = models.ForeignKey(Pedidos, on_delete=models.DO_NOTHING)
  item = models.ForeignKey(Inventario, on_delete=models.DO_NOTHING)
  quantidade = models.IntegerField()
  valor_unitario = models.DecimalField(max_digits=15, decimal_places=2)
  valor_total = models.DecimalField(max_digits=15, decimal_places=2)

