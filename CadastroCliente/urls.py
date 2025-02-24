from django.urls import path
from Cliente import views

urlpatterns = (
    path('', views.index, name='index'),
    path('cadastros/', views.listar_cadastros, name='listar_cadastros'),
    path('cadastro/<int:pk>/', views.detalhar_cadastro, name='detalhar_cadastro'),
    path('cadastro/novo/', views.criar_cadastro, name='criar_cadastro'),
    path('cadastro/<int:pk>/editar/', views.editar_cadastro, name='editar_cadastro'),
    path('cadastro/<int:pk>/deletar/', views.deletar_cadastro, name='deletar_cadastro'),
    path('cadastro/<int:cadastro_id>/endereco/novo/', views.criar_endereco, name='criar_endereco'),
    path('deletar_endereco/<int:endereco_id>/', views.deletar_endereco, name='deletar_endereco'),
)
