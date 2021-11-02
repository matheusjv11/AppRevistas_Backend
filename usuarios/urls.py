# from .views import *
from django.contrib import admin
from django.conf.urls import url
from usuarios.views import *

admin.autodiscover()
admin.site.enable_nav_sidebar = False

app_name = "usuarios"

admin.autodiscover()

urlpatterns = [

    url(r'^usuario/$', UsuarioAppPorIdView.as_view()),
    # Get all
    url(r'^usuarios/$', UserView.as_view(), name='usuarios'),
    # Get:id
    url(r'^usuarios/(?P<pk>\d+)$', SingleUserView.as_view(), name='User-datail'),
    # update:id
    url(r'^usuarios/(?P<pk>\d+)/$', UserUpdateView.as_view(), name='User-update'),

    url(r'^usuarios/(?P<user_id>.+)/artigo/(?P<artigo_id>.+)/favoritar',
        UsuarioAppAddFavsView.as_view()),

    url(r'^usuarios/(?P<user_id>.+)/artigo/(?P<artigo_id>.+)/desfavoritar',
        UsuarioAppRemoveFavsView.as_view()),

    # # # USUARIOS APP
    # url(r'^app-usuarios', UsuarioAppView.as_view(), name='usuarios'),

    # url('^remove-artigofavoritousuario/(?P<user_id>.+)/(?P<artigo_id>.+)',
    #     UsuarioAppRemoveFavsView.as_view()),
    # # url('^add-administrador/(?P<user_id>.+)/$',
    # #     UsuarioAppAddAdminView.as_view()),
    # # url('^remove-administrador/(?P<user_id>.+)/$',
    # #     UsuarioAppRemoveAdminView.as_view()),
    # # url('^add-revistaadministrador/(?P<user_id>.+)/(?P<revista_id>.+)',
    # #     UsuarioAppAddRevistasAdminView.as_view()),
    # # url('^remove-revistaadministrador/(?P<user_id>.+)/(?P<revista_id>.+)',
    # #     UsuarioAppRemoveRevistasAdminView.as_view()),

]
