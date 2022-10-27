from django.urls import path

from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf.urls import include
from .views import Home, Home_Cat_Preco, Del_Cat_Preco, Create_Cat_Preco, Edit_Cat_Preco, Home_Genero, Del_Genero, Create_Genero, Edit_Genero, Home_Clientes, Del_Clientes, Create_Clientes, Edit_Clientes, Home_Inventario, Create_Inventario, Edit_Inventario, Del_Inventario, Home_Pedidos, Create_Pedidos, Del_Pedidos, Edit_Pedidos, Create_Item_Pedido, Del_Item_Pedido

urlpatterns = [
	      path('', login_required(Home.as_view()), name='home'),
              path('cat_preco/', login_required(Home_Cat_Preco.as_view()), name='cat_preco'),
              path('new_cat_preco/', login_required(Create_Cat_Preco.as_view()), name='new_cat_preco'),
              path('del_cat_preco/<int:id>/', permission_required('locadora_admin.delete_cat_preco')(Del_Cat_Preco.as_view()), name='del_cat_preco'),
              path('edit_cat_preco/<int:id>/', permission_required('locadora_admin.change_cat_preco')(Edit_Cat_Preco.as_view()), name='edit_cat_preco'),
              path('genero/', login_required(Home_Genero.as_view()), name='genero'),
              path('new_genero/', login_required(Create_Genero.as_view()), name='new_genero'),
              path('del_genero/<int:id>/', permission_required('locadora_admin.delete_genero')(Del_Genero.as_view()), name='del_genero'),
              path('edit_genero/<int:id>/', permission_required('locadora_admin.change_genero')(Edit_Genero.as_view()), name='edit_genero'),
              path('clientes/', login_required(Home_Clientes.as_view()), name='clientes'),
              path('new_clientes/', login_required(Create_Clientes.as_view()), name='new_clientes'),
              path('del_clientes/<int:id>/', permission_required('locadora_admin.delete_clientes')(Del_Clientes.as_view()), name='del_clientes'),
              path('edit_clientes/<int:id>/', permission_required('locadora_admin.change_clientes')(Edit_Clientes.as_view()), name='edit_clientes'),
              path('inventario/', login_required(Home_Inventario.as_view()), name='inventario'),
              path('new_inventario/', login_required(Create_Inventario.as_view()), name='new_inventario'),
              path('del_inventario/<int:id>/', permission_required('locadora_admin.delete_inventario')(Del_Inventario.as_view()), name='del_inventario'),
              path('edit_inventario/<int:id>/', permission_required('locadora_admin.change_inventario')(Edit_Inventario.as_view()), name='edit_inventario'),
              
              path('pedidos/', login_required(Home_Pedidos.as_view()), name='pedidos'),
              path('new_pedidos/', login_required(Create_Pedidos.as_view()), name='new_pedidos'),
              path('del_pedidos/<int:id>/', permission_required('locadora_admin.delete_inventario')(Del_Pedidos.as_view()), name='del_pedidos'),
              path('edit_pedidos/<int:id>/', permission_required('locadora_admin.change_inventario')(Edit_Pedidos.as_view()), name='edit_pedidos'),
	     
	      path('new_item_pedido/', login_required(Create_Item_Pedido.as_view()), name='new_item_pedido'),
              path('del_item_pedido/<int:id>/', permission_required('locadora_admin.delete_inventario')(Del_Item_Pedido.as_view()), name='del_item_pedido'),

              path('health', views.health, name='health'),
              path('404', views.handler404, name='404'),
              path('500', views.handler500, name='500'),
]
