from __future__ import unicode_literals

from datetime import date
import decimal
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cat_Preco, Genero, Clientes, Inventario, Pedidos, Itens_Pedido
from .forms import Cat_Preco_Form, Genero_Form, Clientes_Form, Inventario_Form, Pedidos_Form, Item_Pedido_Form
from django.utils import timezone
import time
from datetime import datetime, date, time, timedelta

class Home(TemplateView):
   template_name = 'index.html'
   def get(self, request):
       return render(request, self.template_name)

class Home_Cat_Preco(TemplateView):
   template_name = 'cat_preco.html'

   def get(self, request, *args):
       data = Cat_Preco.objects.all()
       for d in data:
           print("Categoria:", d.nome, "  Valor:", d.valor)
       args = {'pub': data}
       return render(request, self.template_name, args)


class Edit_Cat_Preco(LoginRequiredMixin, TemplateView):
   template_name = 'edit_cat_preco.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Cat_Preco, id=id)
       print("post:", post)
       form = Cat_Preco_Form(instance=post)
       data = Cat_Preco.objects.all()
       for d in data:
           print("post:", d.nome, "valor:", d.valor)
       args = {'id': id, 'form': form, 'post': post, 'data': data}
       return render(request, self.template_name, args) 

   def post(self, request, **kwargs):
       cat_preco = get_object_or_404(Cat_Preco, id=int(kwargs['id']))
       if request.method == "POST":
           form = Cat_Preco_Form(request.POST, instance=cat_preco)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('cat_preco')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Del_Cat_Preco(LoginRequiredMixin, TemplateView):
   template_name = 'del_cat_preco.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Cat_Preco, id=id)
       print("post:", post)
       form = Cat_Preco_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       cat_preco = get_object_or_404(Cat_Preco, id=int(kwargs['id']))
       if request.method == "POST":
           form = Cat_Preco_Form(request.POST, instance=cat_preco)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                  # post = form.save(commit=False)
                  # post.save()
                   cat_preco.delete()
                   print("form saved")
                   return redirect('cat_preco')
               else:
                   print("invalid form")
                   print("errors:", form.errors)


class Create_Cat_Preco(LoginRequiredMixin, TemplateView):
   template_name = 'new_cat_preco.html'

   def get(self, request, *args):
       form = Cat_Preco_Form()
       cat_preco = Cat_Preco.objects.all()
       args = {'form': form, 'posts': cat_preco}
       return render(request, self.template_name, args)

   def post(self, request):
       print("inside post")
       if request.method == "POST":
           form = Cat_Preco_Form(request.POST)
           if request.POST.get("submitbtn"):
               print("Submit clicked")
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   #post.nome = request.nome
                   #post.valor = request.valor
                   post.save()
                   print("form saved")
                   return redirect('cat_preco')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Home_Genero(TemplateView):
   template_name = 'genero.html'

   def get(self, request, *args):
       data = Genero.objects.all()
       for d in data:
           print("Genero:", d.nome)
       args = {'pub': data}
       return render(request, self.template_name, args)

class Edit_Genero(LoginRequiredMixin, TemplateView):
   template_name = 'edit_genero.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Genero, id=id)
       print("post:", post)
       form = Genero_Form(instance=post)
       data = Genero.objects.all()
       for d in data:
           print("post:", d.nome)
       args = {'id': id, 'form': form, 'post': post, 'data': data}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       genero = get_object_or_404(Genero, id=int(kwargs['id']))
       if request.method == "POST":
           form = Genero_Form(request.POST, instance=genero)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('genero')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Del_Genero(LoginRequiredMixin, TemplateView):
   template_name = 'del_genero.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Genero, id=id)
       print("post:", post)
       form = Genero_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       genero = get_object_or_404(Genero, id=int(kwargs['id']))
       if request.method == "POST":
           form = Genero_Form(request.POST, instance=genero)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                  # post = form.save(commit=False)
                  # post.save()
                   genero.delete()
                   print("form saved")
                   return redirect('genero')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Create_Genero(LoginRequiredMixin, TemplateView):
   template_name = 'new_genero.html'

   def get(self, request, *args):
       form = Genero_Form()
       genero = Genero.objects.all()
       args = {'form': form, 'posts': genero}
       return render(request, self.template_name, args)

   def post(self, request):
       print("inside post")
       if request.method == "POST":
           form = Genero_Form(request.POST)
           if request.POST.get("submitbtn"):
               print("Submit clicked")
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   #post.nome = request.nome
                   #post.valor = request.valor
                   post.save()
                   print("form saved")
                   return redirect('genero')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Home_Clientes(TemplateView):
   template_name = 'clientes.html'

   def get(self, request, *args):
       data = Clientes.objects.all()
       for d in data:
           print("Nome:", d.nome, " Nasc.:", d.nascimento)
       args = {'pub': data}
       return render(request, self.template_name, args)

class Edit_Clientes(LoginRequiredMixin, TemplateView):
   template_name = 'edit_clientes.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Clientes, id=id)
       print("post:", post)
       form = Clientes_Form(instance=post)
       data = Clientes.objects.all()
       for d in data:
           print("Nome:", d.nome)
       args = {'id': id, 'form': form, 'post': post, 'data': data}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       clientes = get_object_or_404(Clientes, id=int(kwargs['id']))
       if request.method == "POST":
           form = Clientes_Form(request.POST, instance=clientes)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('clientes')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Del_Clientes(LoginRequiredMixin, TemplateView):
   template_name = 'del_clientes.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Clientes, id=id)
       print("post:", post)
       form = Clientes_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       clientes = get_object_or_404(Clientes, id=int(kwargs['id']))
       if request.method == "POST":
           form = Clientes_Form(request.POST, instance=clientes)
           if request.POST.get("submitbtn"):
               #if form.is_valid():
                   print("validating form")
                  # post = form.save(commit=False)
                  # post.save()
                   clientes.delete()
                   print("form saved")
                   return redirect('clientes')
               #else:
               #    print("invalid form")
               #    print("errors:", form.errors)


class Create_Clientes(LoginRequiredMixin, TemplateView):
   template_name = 'new_clientes.html'

   def get(self, request, *args):
       form = Clientes_Form()
       clientes = Clientes.objects.all()
       args = {'form': form, 'posts': clientes}
       return render(request, self.template_name, args)

   def post(self, request):
       print("inside post")
       if request.method == "POST":
           form = Clientes_Form(request.POST)
           if request.POST.get("submitbtn"):
               print("Submit clicked")
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('clientes')
               else:
                   print("invalid form")
                   print("errors:", form.errors)


class Home_Inventario(TemplateView):
   template_name = 'inventario.html'

   def get(self, request, *args):
       data = Inventario.objects.all()
       for d in data:
           print("Titulo:", d.titulo, " Barcode.:", d.barcode, " Gênero:", d.genero)
       args = {'pub': data}
       return render(request, self.template_name, args)

class Edit_Inventario(LoginRequiredMixin, TemplateView):
   template_name = 'edit_inventario.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Inventario, id=id)
       print("post:", post)
       form = Inventario_Form(instance=post)
       data = Inventario.objects.all()
       for d in data:
           print("Nome:", d.titulo)
       args = {'id': id, 'form': form, 'post': post, 'data': data}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       inventario = get_object_or_404(Inventario, id=int(kwargs['id']))
       if request.method == "POST":
           form = Inventario_Form(request.POST, instance=inventario)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('inventario')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Del_Inventario(LoginRequiredMixin, TemplateView):
   template_name = 'del_inventario.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Inventario, id=id)
       print("post:", post)
       form = Inventario_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       inventario = get_object_or_404(Inventario, id=int(kwargs['id']))
       if request.method == "POST":
           form = Inventario_Form(request.POST, instance=inventario)
           if request.POST.get("submitbtn"):
               #if form.is_valid():
                   print("validating form")
                  # post = form.save(commit=False)
                  # post.save()
                   inventario.delete()
                   print("form saved")
                   return redirect('inventario')
               #else:
               #    print("invalid form")
               #    print("errors:", form.errors)



class Create_Inventario(LoginRequiredMixin, TemplateView):
   template_name = 'new_inventario.html'

   def get(self, request, *args):
       form = Inventario_Form()
       inventario = Inventario.objects.all()
       args = {'form': form, 'posts': inventario}
       return render(request, self.template_name, args)

   def post(self, request):
       print("inside post")
       if request.method == "POST":
           form = Inventario_Form(request.POST)
           if request.POST.get("submitbtn"):
               print("Submit clicked")
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('inventario')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Home_Pedidos(TemplateView):
   template_name = 'pedidos.html'

   def get(self, request, *args):
       data = Pedidos.objects.all()
       args = {'pub': data}
       return render(request, self.template_name, args)

class Edit_Pedidos(LoginRequiredMixin, TemplateView):
   template_name = 'edit_pedidos.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Pedidos, id=id)
       print("post:", post)
       form = Pedidos_Form(instance=post)
       data = Pedidos.objects.all()
       itens_pedido = get_object_or_404(Itens_Pedido, id=id)
       for d in data:
           print("ID Pedido:", d.id)
       args = {'id': id, 'form': form, 'post': post, 'data': data}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       pedidos = get_object_or_404(Pedidos, id=int(kwargs['id']))
       if request.method == "POST":
           form = Pedidos_Form(request.POST, instance=pedidos)
           if request.POST.get("submitbtn"):
               if form.is_valid():
                   print("validating form")
                   post = form.save(commit=False)
                   post.save()
                   print("form saved")
                   return redirect('pedidos')
               else:
                   print("invalid form")
                   print("errors:", form.errors)

class Del_Pedidos(LoginRequiredMixin, TemplateView):
   template_name = 'del_pedidos.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Pedidos, id=id)
       print("post:", post)
       form = Pedidos_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       pedidos = get_object_or_404(Pedidos, id=int(kwargs['id']))
       if request.method == "POST":
           form = Pedidos_Form(request.POST, instance=pedidos)
           if request.POST.get("submitbtn"):
               #if form.is_valid():
                   print("validating form")
                  # post = form.save(commit=False)
                  # post.save()
                   pedidos.delete()
                   print("form saved")
                   return redirect('pedidos')
               #else:
               #    print("invalid form")
               #    print("errors:", form.errors)



class Create_Pedidos(LoginRequiredMixin, TemplateView):
   template_name = 'new_pedidos.html'

   def get(self, request, *args, **kwargs):
       form = Pedidos_Form()
       try:
          pedido_id = int(kwargs['id'])
          print ("PEDIDO ID AQUI", pedido_id)      
          pedido = get_object_or_404(Pedidos, id=pedido_id)
          form = Pedidos_Form(instance=pedido)
          itens_pedido = Itens_Pedido.objects.filter(pedido_id=pedido_id)
          #args = {'form': form, 'pedidos': pedidos, 'itens_pedido': itens_pedido}
          init_valor_previsto = decimal.Decimal(sum(itens_pedido.values_list('valor_unitario', flat=True)))
          form.fields['valor_previsto'].initial = init_valor_previsto
          print ("VALORES: ", decimal.Decimal(init_valor_previsto)) # FALTA SOMAR O VALOR TOTAL, DELETAR ITENS DA LISTA E BOTOES DE ADICIONAR O CRIAR PEDIDO CASO JA TENHA FEITO OU NAO
          form.fields['quant_itens_pedido'].initial = pedido.quant_itens_pedido
          print ("QNT ITENS: ", pedido.quant_itens_pedido)
          param = pedido.__dict__
          print (param)
       except KeyError:
 
          pedidos = Pedidos.objects.all()
          if Pedidos.objects.count() != 0:
              pedido_id = Pedidos.objects.all().last().id + 1
              param = {}
          else:
              print("Nao tem")
              pedido_id = 1
              param = {}
      
          itens_pedido = {} 
          form.fields['id'].initial = pedido_id
          form.fields['valor_previsto'].initial = 0
          form.fields['quant_itens_pedido'].initial = 0
          form.fields['data_fechamento'].initial = date.today() + timedelta(days=2)
       args = {'form': form, 'itens_pedido': itens_pedido, 'param': param }
       return render(request, self.template_name, args)

   def post(self, request):
       print("inside post")
       if request.method == "POST":
           form = Pedidos_Form(request.POST)
           id = int(request.POST.get("id"))
           id_cliente = int(request.POST.get("cliente"))
           cliente=cliente = get_object_or_404(Clientes, id=id_cliente)
           user = get_object_or_404(User, id=1)
           dt_prev_fech = datetime.strptime(request.POST.get("data_prev_fechamento"), "%d/%m/%Y").date()
           print("ID CLIENTE: ", id)
           pedido = Pedidos.objects.create(id=id, cliente=cliente, usuario=user, data_abertura=date.today(), data_prev_fechamento=dt_prev_fech,  valor_previsto='0.0', valor_multa=0, observacoes='', pago=False, compra=False, status=True)
           cur_pedido = get_object_or_404(Pedidos, id=id)
           param = cur_pedido.__dict__
           print (param)
           args = {'id': id, 'form': form, 'param': param}
           return render(request, self.template_name, args)

class Create_Item_Pedido(LoginRequiredMixin, TemplateView):
   template_name = 'new_item_pedido.html'

   def get(self, request, *args, **kwargs):
       form = Item_Pedido_Form()
       num_pedido = int(kwargs['id'])
       item_pedido = Itens_Pedido.objects.all()
       args = {'form': form, 'Itens_Pedido': item_pedido, 'id': num_pedido}
       print("Este é o ID !!!", num_pedido) 
       form.fields['pedido'].initial = num_pedido 
       return render(request, self.template_name, args)

   def post(self, request, *args, **kwargs):
       print("inside post")
       if request.method == "POST":
           #form = Item_Pedido_Form(request.POST)
           #args = {'form': form}
           titulo = int(request.POST.get("titulo"))
           id = int(request.POST.get("pedido"))
           if request.POST.get("submitbtn"):
               print("Submit clicked")
               #if form.is_valid():
               #    print("validating form")
               inventario = get_object_or_404(Inventario, id=titulo)
               cat_preco_field_object = inventario._meta.get_field('cat_preco')
               cat_preco_field_value = cat_preco_field_object.value_from_object(inventario)
               preco = get_object_or_404(Cat_Preco, id=cat_preco_field_value)
               cliente = get_object_or_404(Clientes, id=2)
               user = get_object_or_404(User, id=1)
               #if id is !None:
               #pedido = Pedidos.objects.create(id=id, cliente=cliente, usuario=user, data_abertura=date.today(), data_prev_fechamento=date.today() + timedelta(days=2),  valor_previsto=cat_preco_field_value, valor_multa=0, observacoes='', pago=False, compra=False, status=True)
               
               pedido_obj = get_object_or_404(Pedidos, id=id)       

               item_pedido = Itens_Pedido.objects.create(pedido=pedido_obj, item=inventario, quantidade=1, valor_unitario=preco.valor, valor_total = preco.valor * 1) #FALTA FAZER UPDATE DOS ITENS NO PEDIDO E ATUALIZAR SOMAS ETC. DEPOIS EXIBIR A LISTA DOS ITENS EM LOOP

               pedido_obj.valor_previsto = pedido_obj.valor_previsto + preco.valor
               pedido_obj.save()
                
               #return redirect(f'/new_pedidos?id={id}')
               #return redirect(f'{new_pedidos}?{id}=pedido.id')
               return redirect('new_pedidos', id=id)


class Del_Item_Pedido(LoginRequiredMixin, TemplateView):
   template_name = 'del_item_pedido.html'

   def get(self, request, *args, **kwargs):
       id = int(kwargs['id'])
       post = get_object_or_404(Itens_Pedido, id=id)
       print("post:", post)
       form = Item_Pedido_Form(instance=post)
       args = {'id': id, 'form': form, 'post': post}
       return render(request, self.template_name, args)

   def post(self, request, **kwargs):
       itens_pedido = get_object_or_404(Itens_Pedido, id=int(kwargs['id']))
       pedido_id = itens_pedido.pedido_id
       pedido_obj = get_object_or_404(Pedidos, id=pedido_id)
       if request.method == "POST":
           form = Item_Pedido_Form(request.POST, instance=itens_pedido)
           if request.POST.get("submitbtn"):
               print("validating form")
               pedido_obj.valor_previsto = pedido_obj.valor_previsto - itens_pedido.valor_unitario
               pedido_obj.save()
               itens_pedido.delete()
               print("form saved")
               return redirect('new_pedidos', id=pedido_id)
		   

def health(request):
   state = {"status": "UP"}
   return JsonResponse(state)

def handler404(request):
   return render(request, '404.html', status=404)

def handler500(request):
   return render(request, '500.html', status=500)
