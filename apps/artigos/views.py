from apps.artigos.serializers import ArtigosSerializer, AutoresSerializer, AvaliacaoSerializer, PalavrasChaveSerializer
from apps.artigos.models import *
from apps.revistas.models import Edicao
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.filters import SearchFilter

# Create your views here.
#----------- view Autores ------------------------------#

@permission_classes((AllowAny, ))
class AutoresView(ListAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutoresSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','nome_autor']

@permission_classes((AllowAny, ))
class SingleAutoresView(RetrieveAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutoresSerializer

class AutoresUpdateView(RetrieveUpdateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutoresSerializer

#----------- fim view Autores ------------------------------#

#----------- view Artigos ------------------------------#

@permission_classes((AllowAny, ))
class ArtigosView(ListAPIView):
    queryset = Artigo.objects.all()
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
        return Artigo.objects.filter(edicao_id__id=edicao_id)


@permission_classes((AllowAny, ))
class SingleArtigosView(RetrieveAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigosSerializer

class ArtigosUpdateView(RetrieveUpdateAPIView):
    queryset = Artigo.objects.all()
    serializer_class = ArtigosSerializer

#----------- fim view Artigos ------------------------------#

#----------- view Palavras-chave ------------------------------#

@permission_classes((AllowAny, ))
class PalavrasView(ListAPIView):
    queryset = PalavraChave.objects.all()
    serializer_class = PalavrasChaveSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','assunto']

@permission_classes((AllowAny, ))
class SinglePalavrasView(RetrieveAPIView):
    queryset = PalavraChave.objects.all()
    serializer_class = PalavrasChaveSerializer

class PalavrasUpdateView(RetrieveUpdateAPIView):
    queryset = PalavraChave.objects.all()
    serializer_class = PalavrasChaveSerializer

#----------- fim view Palavras-chave ------------------------------#



#----------- view Avaliações ------------------------------#

@permission_classes((AllowAny, ))
class AvaliacoesView(ListAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    #filter_backends=[SearchFilter]
    #search_fields = ['id','nota','id_','autor']


class AvaliacoesCreateView(ListCreateAPIView):
    queryset = Avaliacao.objects.all()
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
        return Edicao.objects.filter(nota=nota)

@permission_classes((AllowAny, ))
class SingleAvaliacoesView(RetrieveAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacoesUpdateView(RetrieveUpdateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

#----------- fim view Avaliações ------------------------------#