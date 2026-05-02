from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página 1 (cadastro)

    path('clientes/', views.lista_clientes, name='lista_clientes'),  # 📄 Página 2

    path('api/clientes/', views.api_clientes, name='api_clientes'),

    path('api/clientes/deletar/<int:id>/', views.deletar_cliente, name='deletar_cliente'),

    path('api/clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
]