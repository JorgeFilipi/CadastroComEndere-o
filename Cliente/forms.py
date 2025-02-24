from django import forms
from .models import CadastroDadosPessoais, EnderecoCliente

class CadastroDadosPessoaisForm(forms.ModelForm):
    class Meta:
        model = CadastroDadosPessoais
        fields = '__all__'

class EnderecoClienteForm(forms.ModelForm):
    class Meta:
        model = EnderecoCliente
        fields = ['rua', 'numero', 'bairro', 'cidade', 'estado', 'cep', 'complemento']
