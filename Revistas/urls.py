
from .views import (
    UserView, 
    SingleUserView,
    UserUpdateView,
    RevistaView, 
    SingleRevistaView,
    RevistaUpdateView, 
    AutoresView,
    SingleAutoresView,
    AutoresUpdateView,
    ArtigosUpdateView,
    ArtigosView,
    ArtigosBYEDICOESIDView,
    SingleArtigosView,
    CategoriaUpdateView,
    CategoriaView,
    SingleCategoriaView,
    EdicoesUpdateView,
    EdicoesView,
    EdicoesIDREVISTAView,
    SingleEdicoesView,
    PalavrasView,
    PalavrasUpdateView,
    SinglePalavrasView,
    ComentariosView,
    ComentariosNoticiaView,
    ComentariosCreateView,
    ComentariosUpdateView,
    SingleComentariosView,
    NoticiasUpdateView,
    NoticiasView,
    NoticiasCreateView,
    SingleNoticiasView,
    AvaliacoesView,
    AvaliacoesCreateView,
    AvaliacoesUpdateView,
    AvaliacoesNOTAView,
    SingleAvaliacoesView,
    UsuarioAppView,
    UsuarioAppPorIdView,
    UsuarioAppAddFavsView,
    UsuarioAppRemoveFavsView,
    UsuarioAppAddAdminView,
    UsuarioAppRemoveAdminView,
    UsuarioAppAddRevistasAdminView,
    UsuarioAppRemoveRevistasAdminView,
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
    url(r'^update-autores/(?P<pk>\d+)', AutoresUpdateView.as_view(),name='autores-update'),
    
    #REVISTAS
    url(r'^revistas', RevistaView.as_view(),name='revistas'),
    url(r'^detail-revistas/(?P<pk>\d+)', SingleRevistaView.as_view(),name='revista-datail'),
    url(r'^update-revistas/(?P<pk>\d+)', RevistaUpdateView.as_view(),name='revista-update'),

    #ARTIGOS
    url(r'^artigos', ArtigosView.as_view(),name='artigos'),
    url('^get-artigosdaedicao/(?P<edicao_id>.+)/$', ArtigosBYEDICOESIDView.as_view()),
    url(r'^detail-artigos/(?P<pk>\d+)', SingleArtigosView.as_view(),name='artigos-datail'),
    url(r'^update-artigos/(?P<pk>\d+)', ArtigosUpdateView.as_view(),name='artigos-update'),

    #CATEGORIA
    url(r'^categorias', CategoriaView.as_view(),name='categorias'),
    url(r'^detail-categorias/(?P<pk>\d+)', SingleCategoriaView.as_view(),name='categorias-datail'),
    url(r'^update-categorias/(?P<pk>\d+)', CategoriaUpdateView.as_view(),name='categorias-update'),

    #EDICOES
    url(r'^edicoes', EdicoesView.as_view(),name='edicoes'),
    url('^get-edicoesdarevista/(?P<revista_id>.+)/$', EdicoesIDREVISTAView.as_view()),
    url(r'^detail-edicoes/(?P<pk>\d+)', SingleEdicoesView.as_view(),name='edicoes-datail'),
    url(r'^update-edicoes/(?P<pk>\d+)', EdicoesUpdateView.as_view(),name='edicoes-update'),

    #PALAVRAS-CHAVE
    url(r'^palavras', PalavrasView.as_view(),name='palavras'),
    url(r'^detail-palavras/(?P<pk>\d+)', SinglePalavrasView.as_view(),name='palavras-datail'),
    url(r'^update-palavras/(?P<pk>\d+)', PalavrasUpdateView.as_view(),name='palavras-update'),

    #COMENTARIOS
    url(r'^comentarios', ComentariosView.as_view(),name='comentarios'),
    url('^get-comentariosnoticia/(?P<noticia_id>.+)/$', ComentariosNoticiaView.as_view()),
    url(r'^create-comentarios/', ComentariosCreateView.as_view(),name='comentarios-create'),
    url(r'^detail-comentarios/(?P<pk>\d+)', SingleComentariosView.as_view(),name='comentarios-datail'),
    url(r'^update-comentarios/(?P<pk>\d+)', ComentariosUpdateView.as_view(),name='comentarios-update'),
    

    #NOTICIAS
    url(r'^noticias', NoticiasView.as_view(),name='noticias'),
    url(r'^create-noticias/', NoticiasCreateView.as_view(),name='noticias-create'),
    url(r'^detail-noticias/(?P<pk>\d+)', SingleNoticiasView.as_view(),name='noticias-datail'),
    url(r'^update-noticias/(?P<pk>\d+)', NoticiasUpdateView.as_view(),name='noticias-update'),
   
    #AVALIACOES
    url(r'^avaliacoes', AvaliacoesView.as_view(),name='avaliacoes'),
    url('^get-avaliacoespornota/(?P<nota>.+)/$', AvaliacoesNOTAView.as_view()),
    url(r'^create-avaliacoes/', AvaliacoesCreateView.as_view(),name='avaliacoes-create'),
    url(r'^detail-avaliacoes/(?P<pk>\d+)', SingleAvaliacoesView.as_view(),name='avaliacoes-datail'),
    url(r'^update-avaliacoes/(?P<pk>\d+)', AvaliacoesUpdateView.as_view(),name='avaliacoes-update'),

    #USUARIOS
    url(r'^usuarios', UserView.as_view(),name='usuarios'),
    url(r'^detail-user/(?P<pk>\d+)', SingleUserView.as_view(),name='User-datail'),
    url(r'^update-user/(?P<pk>\d+)', UserUpdateView.as_view(),name='User-update'),
   

    #USUARIOS APP
    url(r'^app-usuarios', UsuarioAppView.as_view(),name='usuarios'),
    url('^get-usuariosporid/(?P<user_id>.+)/$', UsuarioAppPorIdView.as_view()),
    url('^add-artigofavoritousuario/(?P<user_id>.+)/(?P<artigo_id>.+)', UsuarioAppAddFavsView.as_view()),
    url('^remove-artigofavoritousuario/(?P<user_id>.+)/(?P<artigo_id>.+)', UsuarioAppRemoveFavsView.as_view()),
    url('^add-administrador/(?P<user_id>.+)/$', UsuarioAppAddAdminView.as_view()),
    url('^remove-administrador/(?P<user_id>.+)/$', UsuarioAppRemoveAdminView.as_view()),
    url('^add-revistaadministrador/(?P<user_id>.+)/(?P<revista_id>.+)', UsuarioAppAddRevistasAdminView.as_view()),
    url('^remove-revistaadministrador/(?P<user_id>.+)/(?P<revista_id>.+)', UsuarioAppRemoveRevistasAdminView.as_view()),
    #url(r'^detail-noticias/(?P<pk>\d+)', SingleNoticiasView.as_view(),name='noticias-datail'),
    #url(r'^update-noticias/(?P<pk>\d+)', NoticiasUpdateView.as_view(),name='noticias-update'),
    #url(r'^delete-noticias/(?P<pk>\d+)', NoticiasDeleteView.as_view(),name='noticias-delete'),

    
]