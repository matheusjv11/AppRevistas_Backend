from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.generics import *
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import permission_classes

# ---------------------------------

"""
    -Nesse arquivo consta as configurações de como cada tabela do banco de dados vai ser disposta na API 
    fornecida por 'serializers' do RestFramework.
   
    -O comando @permission_classes((AllowAny, )) faz com quem qualquer pessoa tenha acesso à essa página
    da API, caso contrário, o acesso se dá apenas mediante à uma autenticação.

    -Quando for criar um novo usuário, a UserView será chamada pra criar um usuário padrão Django, e automaticamente
    será criado tambem um UsuarioAPP.
"""

#------ views de Revistas--------------------------------#


@permission_classes((AllowAny, ))
class RevistaView(ListAPIView):
    queryset = Revista.objects.all().exclude(nome_revista_portugues='Not found')
    serializer_class = RevistaSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'issn',
                     'nome_revista_portugues', 'nome_revista_english']


@permission_classes((AllowAny, ))
class SingleRevistaView(RetrieveAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer


class RevistaUpdateView(RetrieveUpdateAPIView):
    queryset = Revista.objects.all()
    serializer_class = RevistaSerializer

#------ fim views de Revistas--------------------------------#

#----------- view Categoria ------------------------------#


@permission_classes((AllowAny, ))
class CategoriaView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'nome_categoria']


@permission_classes((AllowAny, ))
class SingleCategoriaView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaUpdateView(RetrieveUpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#----------- fim view Categoria ------------------------------#

#----------- view Edicoes ------------------------------#


@permission_classes((AllowAny, ))
class EdicoesView(ListAPIView):
    queryset = Edicao.objects.all()
    serializer_class = EdicoesSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'edicao_portugues',
                     'edicao_english', 'data_lancamento']


@permission_classes((AllowAny, ))
class EdicoesIDREVISTAView(ListCreateAPIView):
    #queryset = Edicoes.objects.all()
    serializer_class = EdicoesSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['data_lancamento']

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        revista_id = self.kwargs['revista_id']
        return Edicao.objects.filter(revista_id__id=revista_id)


@permission_classes((AllowAny, ))
class SingleEdicoesView(RetrieveAPIView):
    queryset = Edicao.objects.all()
    serializer_class = EdicoesSerializer


class EdicoesUpdateView(RetrieveUpdateAPIView):
    queryset = Edicao.objects.all()
    serializer_class = EdicoesSerializer

#----------- fim view Edicoes ------------------------------#
