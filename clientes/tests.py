from django.test import TestCase
from .models import Cliente

class ClienteTest(TestCase):
    def test_criar_cliente(self):
        cliente = Cliente.objects.create(
            nome_completo="Teste",
            idade=20,
            telefone="123456"
        )
        self.assertEqual(cliente.nome_completo, "Teste")    