
# from .views import *
from apps.revistas.views import *
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include,url
from rest_framework.authtoken import views

app_name = "revistas"

urlpatterns = [
    #REVISTAS
    url(r'^revistas/$', RevistaView.as_view(),name='revistas'),
    url(r'^revistas/(?P<pk>\d+)/$', SingleRevistaView.as_view(),name='revista-datail'),
    # url(r'^revistas/(?P<pk>\d+)/update/$', RevistaUpdateView.as_view(),name='revista-update'),

    #CATEGORIA
    url(r'^categorias/$', CategoriaView.as_view(),name='categorias'),
    url(r'^categorias/(?P<pk>\d+)/$', SingleCategoriaView.as_view(),name='categorias-datail'),
    # url(r'^update-categorias/(?P<pk>\d+)', CategoriaUpdateView.as_view(),name='categorias-update'),

    #EDICOES
    url(r'^edicoes/$', EdicoesView.as_view(),name='edicoes'),
    url(r'^revistas/(?P<revista_id>.+)/edicoes/$', EdicoesIDREVISTAView.as_view()),
    url(r'^edicoes/(?P<pk>\d+)/$', SingleEdicoesView.as_view(),name='edicoes-datail'),
    # url(r'^edicoes/(?P<pk>\d+)/update/$', EdicoesUpdateView.as_view(),name='edicoes-update'),
]
