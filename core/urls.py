from django.contrib import admin
from django.urls import path, include   # 👈 AQUI você adiciona o include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),  # 👈 AQUI conecta seu app
]