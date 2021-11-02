
# from .views import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include,url
from rest_framework.authtoken import views
from artigos.views import *

app_name = "artigos"

urlpatterns = [

    #AUTORES
    url(r'^autores/$', AutoresView.as_view(),name='autores'),
    url(r'^autores/(?P<pk>\d+)/$', SingleAutoresView.as_view(),name='autores-datail'),
    url(r'^autores/(?P<pk>\d+)/update/$', AutoresUpdateView.as_view(),name='autores-update'),

    #ARTIGOS
    url(r'^artigos/$', ArtigosView.as_view(),name='artigos'),
    url(r'^artigos/(?P<pk>\d+)/$', SingleArtigosView.as_view(),name='artigos-datail'),
    url(r'^artigos/(?P<pk>\d+)/$', ArtigosUpdateView.as_view(),name='artigos-update'),
    url(r'^artigos/(?P<edicao_id>.+)/edicao/$', ArtigosBYEDICOESIDView.as_view()),

    #PALAVRAS-CHAVE
    url(r'^palavras/$', PalavrasView.as_view(),name='palavras'),
    url(r'^palavras/(?P<pk>\d+)/$', SinglePalavrasView.as_view(),name='palavras-datail'),
    url(r'^palavras/(?P<pk>\d+)/update/$', PalavrasUpdateView.as_view(),name='palavras-update'),
       
    #AVALIACOES
    url(r'^avaliacoes/$', AvaliacoesView.as_view(),name='avaliacoes'),
    # url('^get-avaliacoespornota/(?P<nota>.+)/$', AvaliacoesNOTAView.as_view()),
    url(r'^avaliacoes/create/$', AvaliacoesCreateView.as_view(),name='avaliacoes-create'),
    url(r'^avaliacoes/(?P<pk>\d+)/$', SingleAvaliacoesView.as_view(),name='avaliacoes-datail'),
    url(r'^avaliacoes/(?P<pk>\d+)/update/$', AvaliacoesUpdateView.as_view(),name='avaliacoes-update'),

]


