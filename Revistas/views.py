from django.shortcuts import render
from rest_framework import viewsets, generics
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    UserLoginSerializer,
    UserUpdateSerializer,
    RevistaSerializer,
    AutoresSerializer,
    ArtigosSerializer,
    CategoriaSerializer,
    EdicoesSerializer,
    PalavrasChaveSerializer,
    NoticiasViewSerializer,
    NoticiasCreateSerializer,
    ComentariosSerializer,
    AvaliacaoSerializer,
    UsuarioAppSerializer,
    )

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny

from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    ListCreateAPIView, 
    RetrieveAPIView,
    GenericAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    )

from Revistas.models import Autores, Avaliacoes,Artigos,Categoria,Edicoes,Revista,Palavras_chave, Noticias, Comentarios, Usuario
from django.db.models import Q
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import JSONParser, MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.decorators import authentication_classes, permission_classes
import json
from rest_framework import status

#------ views de Usuarios --------

User = get_user_model()

@permission_classes((AllowAny, ))
class UserView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends=[SearchFilter]
    search_fields = ['username']


@permission_classes((AllowAny, ))
class SingleUserView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(RetrieveUpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

#------ views de Revistas--------

@permission_classes((AllowAny, ))
class RevistaView(ListAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','issn','nome_revista_portugues','nome_revista_english']

@permission_classes((AllowAny, ))
class SingleRevistaView(RetrieveAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer

class RevistaUpdateView(RetrieveUpdateAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer

"""class AutoresDeleteView(DestroyAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer"""

#----------- view Autores --------------

@permission_classes((AllowAny, ))
class AutoresView(ListAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','nome_autor']

@permission_classes((AllowAny, ))
class SingleAutoresView(RetrieveAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class AutoresUpdateView(RetrieveUpdateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer


#----------- view Artigos --------------

@permission_classes((AllowAny, ))
class ArtigosView(ListAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo_portugues','titulo_english','descricao_portugues','descricao_english','categoria_id__nome_categoria']

@permission_classes((AllowAny, ))
class ArtigosBYEDICOESIDView(ListAPIView):
    #queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    #filter_backends=[SearchFilter]
    #search_fields = ['edicao_id__id']

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        edicao_id = self.kwargs['edicao_id']
        return Artigos.objects.filter(edicao_id__id=edicao_id)

@permission_classes((AllowAny, ))
class SingleArtigosView(RetrieveAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

class ArtigosUpdateView(RetrieveUpdateAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer


#----------- view Categoria --------------

@permission_classes((AllowAny, ))
class CategoriaView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','nome_categoria']

@permission_classes((AllowAny, ))
class SingleCategoriaView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaUpdateView(RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


#----------- view Edicoes --------------

@permission_classes((AllowAny, ))
class EdicoesView(ListAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','edicao_portugues','edicao_english','data_lancamento']

@permission_classes((AllowAny, ))
class EdicoesIDREVISTAView(ListCreateAPIView):
    #queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter, OrderingFilter]
    search_fields = ['data_lancamento']

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        revista_id = self.kwargs['revista_id']
        return Edicoes.objects.filter(revista_id__id=revista_id)

@permission_classes((AllowAny, ))
class SingleEdicoesView(RetrieveAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

class EdicoesUpdateView(RetrieveUpdateAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer



#----------- view Palavras-chave --------------

@permission_classes((AllowAny, ))
class PalavrasView(ListAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','assunto']

@permission_classes((AllowAny, ))
class SinglePalavrasView(RetrieveAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

class PalavrasUpdateView(RetrieveUpdateAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

#----------- view Comentario --------------

@permission_classes((AllowAny, ))
class ComentariosView(ListAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','corpo']


class ComentariosCreateView(ListCreateAPIView):

    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','corpo']

    #def perform_create(self, serializer):
        #serializer.save(autor=self.request.user.id)

@permission_classes((AllowAny, ))
class SingleComentariosView(RetrieveAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

class ComentariosUpdateView(RetrieveUpdateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer


#----------- view Noticias --------------

@permission_classes((AllowAny, ))
class NoticiasView(ListAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasViewSerializer
    parser_classes = (MultiPartParser, JSONParser)

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo','corpo','autor']


class NoticiasCreateView(CreateAPIView):
    
    queryset = Noticias.objects.all()
    serializer_class = NoticiasCreateSerializer
    #parser_classes = (MultiPartParser, JSONParser)

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo','corpo','autor']




@permission_classes((AllowAny, ))
class SingleNoticiasView(RetrieveAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasViewSerializer

class NoticiasUpdateView(RetrieveUpdateAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasViewSerializer


#----------- view Avaliações --------------

@permission_classes((AllowAny, ))
class AvaliacoesView(ListAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    #filter_backends=[SearchFilter]
    #search_fields = ['id','nota','id_','autor']


class AvaliacoesCreateView(ListCreateAPIView):
    
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer
    

@permission_classes((AllowAny, ))
class AvaliacoesNOTAView(ListAPIView):
    #queryset = Edicoes.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        nota = self.kwargs['nota']
        return Edicoes.objects.filter(nota=nota)

@permission_classes((AllowAny, ))
class SingleAvaliacoesView(RetrieveAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacoesUpdateView(RetrieveUpdateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer


#----------- view Usuario APP --------------

@permission_classes((AllowAny, ))
class UsuarioAppView(ListAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioAppSerializer

@permission_classes((AllowAny, ))
class UsuarioAppPorIdView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        user_id = self.kwargs['user_id']
        return Usuario.objects.filter(user_id=user_id)

class UsuarioAppAddFavsView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        artigo_id = self.kwargs.get('artigo_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        artigo_OBJ  = Artigos.objects.get(id=artigo_id)


        usuario_OBJ.artigos_favoritos.add(artigo_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)
    
class UsuarioAppRemoveFavsView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        artigo_id = self.kwargs.get('artigo_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        artigo_OBJ  = Artigos.objects.get(id=artigo_id)


        usuario_OBJ.artigos_favoritos.remove(artigo_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)


class UsuarioAppAddAdminView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        usuario_OBJ = Usuario.objects.get(id=usuario_id)    
        usuario_OBJ.administrador = True
        usuario_OBJ.save()
        
        return Usuario.objects.filter(id=usuario_id)


class UsuarioAppRemoveAdminView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        usuario_OBJ = Usuario.objects.get(id=usuario_id)    
        usuario_OBJ.administrador = False
        usuario_OBJ.save()
        
        return Usuario.objects.filter(id=usuario_id)


class UsuarioAppAddRevistasAdminView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        revista_id = self.kwargs.get('revista_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        if usuario_OBJ.administrador == False:
            return "render(HTTP_400_BAD_REQUEST, template_name=HTTP_200_OK)"

        revista_OBJ = Revista.objects.get(id=revista_id)
        usuario_OBJ.gerencia_revista.add(revista_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)


class UsuarioAppRemoveRevistasAdminView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        revista_id = self.kwargs.get('revista_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        if usuario_OBJ.administrador == False:
            return "render(HTTP_400_BAD_REQUEST, template_name=HTTP_200_OK)"

        revista_OBJ = Revista.objects.get(id=revista_id)
        usuario_OBJ.gerencia_revista.remove(revista_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)