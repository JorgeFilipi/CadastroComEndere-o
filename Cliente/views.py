from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from .models import CadastroDadosPessoais, EnderecoCliente
from .forms import CadastroDadosPessoaisForm, EnderecoClienteForm


def index(request):
    return render(request, 'index.html')


def listar_cadastros(request):
    cadastros = CadastroDadosPessoais.objects.all()
    return render(request, 'listar_cadastros.html', {'cadastros': cadastros})


def detalhar_cadastro(request, pk):
    cadastro = get_object_or_404(CadastroDadosPessoais, pk=pk)
    endereco_cliente = cadastro.endereco_cliente.all()
    return render(request, 'detalhar_cadastro.html', {'cadastro': cadastro, 'endereco_cliente': endereco_cliente})


def criar_cadastro(request):
    if request.method == "POST":
        form = CadastroDadosPessoaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cadastros')
    else:
        form = CadastroDadosPessoaisForm()
    return render(request, 'criar_cadastro.html', {'form': form})


def editar_cadastro(request, pk):
    cadastro = get_object_or_404(CadastroDadosPessoais, pk=pk)
    if request.method == "POST":
        form = CadastroDadosPessoaisForm(request.POST, instance=cadastro)
        if form.is_valid():
            form.save()
            return redirect('listar_cadastros')
    else:
        form = CadastroDadosPessoaisForm(instance=cadastro)
    return render(request, 'editar_cadastro.html', {'form': form})


def deletar_cadastro(request, pk):
    cadastro = get_object_or_404(CadastroDadosPessoais, pk=pk)
    if request.method == "POST":
        cadastro.delete()
        return redirect('listar_cadastros')
    return render(request, 'deletar_cadastro.html', {'cadastro': cadastro})


def deletar_endereco(request, endereco_id):
    endereco = get_object_or_404(EnderecoCliente, id=endereco_id)
    cadastro_id = endereco.nome.id
    endereco.delete()
    return redirect(reverse('detalhar_cadastro', args=[cadastro_id]))

def criar_endereco(request, cadastro_id):
    cadastro = get_object_or_404(CadastroDadosPessoais, id=cadastro_id)
    if request.method == "POST":
        form = EnderecoClienteForm(request.POST)
        if form.is_valid():
            endereco = form.save(commit=False)
            endereco.nome = cadastro
            endereco.save()
            return redirect('detalhar_cadastro', pk=cadastro.id)
    else:
        form = EnderecoClienteForm()
    return render(request, 'criar_endereco.html', {'form': form, 'cadastro': cadastro})
