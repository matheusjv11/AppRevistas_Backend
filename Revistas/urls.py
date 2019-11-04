
from .views import (
    UserView,
    UserLoginView, 
    SingleUserView,
    RevistaView, 
    SingleRevistaView,
    RevistaUpdateView, 
    AutoresView,
    SingleAutoresView,
    AutoresDeleteView,
    AutoresUpdateView,
    ArtigosDeleteView,
    ArtigosUpdateView,
    ArtigosView,
    SingleArtigosView,
    CategoriaDeleteView,
    CategoriaUpdateView,
    CategoriaView,
    SingleCategoriaView,
    EdicoesUpdateView,
    EdicoesView,
    SingleEdicoesView,
    PalavrasView,
    PalavrasUpdateView,
    SinglePalavrasView,
    ComentariosView,
    ComentariosUpdateView,
    ComentariosDeleteView,
    SingleComentariosView,
    NoticiasDeleteView,
    NoticiasUpdateView,
    NoticiasView,
    SingleNoticiasView,
     )

from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include,url
from rest_framework.authtoken import views
from Revistas.views import UserView,RevistaView

app_name = "Revistas"

urlpatterns = [

    #AUTORES
    url(r'^autores', AutoresView.as_view(),name='autores'),
    url(r'^detail-autores/(?P<pk>\d+)', SingleAutoresView.as_view(),name='autores-datail'),
    url(r'^delete-autores/(?P<pk>\d+)', AutoresDeleteView.as_view(),name='autores-delete'),
    url(r'^update-autores/(?P<pk>\d+)', AutoresUpdateView.as_view(),name='autores-update'),
    
    #REVISTAS
    url(r'^revistas', RevistaView.as_view(),name='revistas'),
    url(r'^detail-revistas/(?P<pk>\d+)', SingleRevistaView.as_view(),name='revista-datail'),
    url(r'^update-revistas/(?P<pk>\d+)', RevistaUpdateView.as_view(),name='revista-update'),

    #ARTIGOS
    url(r'^artigos', ArtigosView.as_view(),name='artigos'),
    url(r'^detail-artigos/(?P<pk>\d+)', SingleArtigosView.as_view(),name='artigos-datail'),
    url(r'^delete-artigos/(?P<pk>\d+)', ArtigosDeleteView.as_view(),name='artigos-delete'),
    url(r'^update-artigos/(?P<pk>\d+)', ArtigosUpdateView.as_view(),name='artigos-update'),

    #CATEGORIA
    url(r'^categorias', CategoriaView.as_view(),name='categorias'),
    url(r'^detail-categorias/(?P<pk>\d+)', SingleCategoriaView.as_view(),name='categorias-datail'),
    url(r'^delete-categorias/(?P<pk>\d+)', CategoriaDeleteView.as_view(),name='categorias-delete'),
    url(r'^update-categorias/(?P<pk>\d+)', CategoriaUpdateView.as_view(),name='categorias-update'),

    #EDICOES
    url(r'^edicoes', EdicoesView.as_view(),name='edicoes'),
    url(r'^detail-edicoes/(?P<pk>\d+)', SingleEdicoesView.as_view(),name='edicoes-datail'),
    url(r'^update-edicoes/(?P<pk>\d+)', EdicoesUpdateView.as_view(),name='edicoes-update'),

    #PALAVRAS-CHAVE
    url(r'^palavras', PalavrasView.as_view(),name='palavras'),
    url(r'^detail-palavras/(?P<pk>\d+)', SinglePalavrasView.as_view(),name='palavras-datail'),
    url(r'^update-palavras/(?P<pk>\d+)', PalavrasUpdateView.as_view(),name='palavras-update'),

    #COMENTARIOS
    url(r'^comentarios', ComentariosView.as_view(),name='comentarios'),
    url(r'^detail-comentarios/(?P<pk>\d+)', SingleComentariosView.as_view(),name='comentarios-datail'),
    url(r'^update-comentarios/(?P<pk>\d+)', ComentariosUpdateView.as_view(),name='comentarios-update'),
    url(r'^delete-comentarios/(?P<pk>\d+)', ComentariosDeleteView.as_view(),name='comentarios-delete'),

    #NOTICIAS
    url(r'^noticias', NoticiasView.as_view(),name='noticias'),
    url(r'^detail-noticias/(?P<pk>\d+)', SingleNoticiasView.as_view(),name='noticias-datail'),
    url(r'^update-noticias/(?P<pk>\d+)', NoticiasUpdateView.as_view(),name='noticias-update'),
    url(r'^delete-noticias/(?P<pk>\d+)', NoticiasDeleteView.as_view(),name='noticias-delete'),

    #USUARIOS
    url(r'^usuarios', UserView.as_view(),name='usuarios'),
    url(r'^login', UserLoginView.as_view(),name='login'),
    #url(r'^detail-noticias/(?P<pk>\d+)', SingleNoticiasView.as_view(),name='noticias-datail'),
    #url(r'^update-noticias/(?P<pk>\d+)', NoticiasUpdateView.as_view(),name='noticias-update'),
    #url(r'^delete-noticias/(?P<pk>\d+)', NoticiasDeleteView.as_view(),name='noticias-delete'),

    
]