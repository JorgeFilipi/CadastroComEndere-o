from django.db import models
from django.shortcuts import render


class CadastroDadosPessoais(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.nome} {self.sobrenome} {self.cpf} {self.email} {self.telefone}"

class EnderecoCliente(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    nome = models.ForeignKey('CadastroDadosPessoais', on_delete=models.CASCADE, related_name='endereco_cliente')

    def __str__(self):
        return f"{self.rua} {self.numero} {self.bairro} {self.cidade} {self.estado} {self.cep} {self.complemento}"


