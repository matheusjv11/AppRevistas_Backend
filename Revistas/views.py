from django.shortcuts import render
from rest_framework import viewsets, generics
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import (
    UserSerializer,
    UserLoginSerializer,
    RevistaSerializer,
    AutoresSerializer,
    ArtigosSerializer,
    CategoriaSerializer,
    EdicoesSerializer,
    PalavrasChaveSerializer,
    NoticiasSerializer,
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

#------ views de Usuarios --------

User = get_user_model()
class UserView(ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer



class SingleUserView(RetrieveAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(APIView):
    
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def POST(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


#------ views de Revistas--------

class RevistaView(ListCreateAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','issn','nome_revista_portugues','nome_revista_english']

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

class AutoresView(ListCreateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','nome_autor']

class SingleAutoresView(RetrieveAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class AutoresUpdateView(RetrieveUpdateAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

"""class AutoresDeleteView(RetrieveDestroyAPIView):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer"""

#----------- view Artigos --------------

class ArtigosView(ListCreateAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo_portugues','titulo_english','descricao_portugues','descricao_english','categoria_id__nome_categoria']

class ArtigosBYEDICOESIDView(ListCreateAPIView):
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

class SingleArtigosView(RetrieveAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

class ArtigosUpdateView(RetrieveUpdateAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer

"""class ArtigosDeleteView(RetrieveDestroyAPIView):
    queryset = Artigos.objects.all()
    serializer_class = ArtigosSerializer"""

#----------- view Categoria --------------

class CategoriaView(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','nome_categoria']

class SingleCategoriaView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaUpdateView(RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

"""class CategoriaDeleteView(RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer"""

#----------- view Edicoes --------------

class EdicoesView(ListCreateAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','edicao_portugues','edicao_english','data_lancamento']

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

class SingleEdicoesView(RetrieveAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

class EdicoesUpdateView(RetrieveUpdateAPIView):
    queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

"""class CategoriaDeleteView(DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer"""

#----------- view Palavras-chave --------------

class PalavrasView(ListCreateAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','assunto']

class SinglePalavrasView(RetrieveAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

class PalavrasUpdateView(RetrieveUpdateAPIView):
    queryset = Palavras_chave.objects.all()
    serializer_class = PalavrasChaveSerializer

"""class CategoriaDeleteView(DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer"""

#----------- view Comentario --------------

class ComentariosView(ListCreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','corpo']

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user.id)

class SingleComentariosView(RetrieveAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

class ComentariosUpdateView(RetrieveUpdateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer

"""class ComentariosDeleteView(RetrieveDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer"""

#----------- view Noticias --------------

class NoticiasView(ListCreateAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer
    parser_classes = (MultiPartParser, JSONParser)

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo','corpo','autor']

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user.id)




class SingleNoticiasView(RetrieveAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer

class NoticiasUpdateView(RetrieveUpdateAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer

    
 
"""class NoticiasDeleteView(RetrieveDestroyAPIView):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer """

#----------- view Avaliações --------------

class AvaliacoesView(ListCreateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    #filter_backends=[SearchFilter]
    #search_fields = ['id','nota','id_','autor']

    def perform_create(self, serializer):
        serializer.save(id_usuario=self.request.user.id)

class AvaliacoesNOTAView(ListCreateAPIView):
    #queryset = Edicoes.objects.all()
    serializer_class = AvaliacaoSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        nota = self.kwargs['nota']
        return Edicoes.objects.filter(nota=nota)

class SingleAvaliacoesView(RetrieveAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacoesUpdateView(RetrieveUpdateAPIView):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer


#----------- view Usuario APP --------------

class UsuarioAppView(ListAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioAppSerializer

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

