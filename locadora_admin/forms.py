from django import forms
from .models import Cat_Preco 
from .models import Genero
from .models import Clientes
from .models import Inventario
from .models import Midia
from django.forms import ModelChoiceField

class NameChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return f'{obj.nome}'

class Cat_Preco_Form(forms.ModelForm):
   nome = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o nome da categoria', 'class': 'form-control'}
   ))
   valor = forms.DecimalField(required=True, max_digits=8, decimal_places=2, localize=True)
   

   class Meta:
       model = Cat_Preco
       fields = ('nome', 'valor')

class Genero_Form(forms.ModelForm):
   nome = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o nome do gênero', 'class': 'form-control'}
   ))
   
   class Meta:
       model = Genero
       fields = ('nome',)

class Clientes_Form(forms.ModelForm):
   nome = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o nome do cliente', 'class': 'form-control'}
   ))
   
   nascimento = forms.DateField(
    widget=forms.DateInput(format='%d/%m/%Y', attrs={'class': "input", 'placeholder': "Ex.: dd/mm/aaaa", 'data-mask': "##/##/####"}))
 
        

   endereco = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o endereço do cliente', 'class': 'form-control'}
   ))

   cep = forms.CharField(required=True, max_length=9, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o CEP', 'class': 'form-control'}
   ))

   telefone = forms.CharField(required=True, max_length=20, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o telefone', 'class': 'form-control'}
   ))
 
   email = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o email', 'class': 'form-control'}
   ))
   cpf = forms.CharField(required=True, max_length=11, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o CPF', 'class': 'form-control'}
   ))

   fator_multa = forms.DecimalField(required=True, max_digits=8, decimal_places=2, localize=True)

   pontos_fidelidade = forms.DecimalField(required=True, max_digits=8, decimal_places=0, localize=True)

  
   class Meta:
       model = Clientes
       fields = ('nome', 'nascimento', 'endereco', 'cep', 'telefone', 'email', 'cpf', 'fator_multa', 'pontos_fidelidade', )

class Inventario_Form(forms.ModelForm):
   titulo = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite títilo do filme/programa/media', 'class': 'form-control'}
   ))

   barcode = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
       attrs={'placeholder': 'Digite o codigo de barras', 'class': 'form-control'}
   ))

   genero = NameChoiceField(queryset=Genero.objects.all())

   class_indicativa = forms.DecimalField(required=True, max_digits=8, decimal_places=0, localize=True)

   total_estoque = forms.DecimalField(required=True, max_digits=8, decimal_places=0, localize=True)

   total_disponivel = forms.DecimalField(required=True, max_digits=8, decimal_places=0, localize=True)
   
   midia =  NameChoiceField(queryset=Midia.objects.all())

   max_dias = forms.DecimalField(required=True, max_digits=8, decimal_places=0, localize=True)

   cat_preco = NameChoiceField(queryset=Cat_Preco.objects.all())

   preco_venda = forms.DecimalField(required=True, max_digits=8, decimal_places=2, localize=True)

   class Meta:
       model = Inventario
       fields = ('titulo', 'barcode', 'genero', 'class_indicativa', 'total_estoque', 'total_disponivel', 'midia', 'max_dias', 'cat_preco', 'preco_venda', )
