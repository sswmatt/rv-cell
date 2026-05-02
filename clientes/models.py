from django.db import models

class Cliente(models.Model):
    nome_completo = models.CharField(max_length=150)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_completo