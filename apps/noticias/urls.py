from django.conf.urls import url
from apps.noticias.views import *

app_name = "noticias"

urlpatterns = [

    # COMENTARIOS
    url(r'^comentarios/$', ComentariosView.as_view(), name='comentarios'),
    url(r'^comentarios/(?P<noticia_id>\d+)/$', ComentariosNoticiaView.as_view()),
    url(r'^comentarios/create/$', ComentariosCreateView.as_view(),
        name='comentarios-create'),
    url(r'^comentarios/(?P<pk>\d+)/update/$',
        ComentariosUpdateView.as_view(), name='comentarios-update'),

    # NOTICIAS
    url(r'^noticias/$', NoticiasView.as_view(), name='noticias'),
    url(r'^noticias/(?P<pk>\d+)/$',
        SingleNoticiasView.as_view(), name='noticias-datail'),
    url(r'^noticias/create/$', NoticiasCreateView.as_view(), name='noticias-create'),
    url(r'^noticias/(?P<pk>\d+)/update/$',
        NoticiasUpdateView.as_view(), name='noticias-update'),
]

# url(r'^comentarios/(?P<pk>\d+)/$', SingleComentariosView.as_view(),name='comentarios-datail'),
