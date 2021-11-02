# from django.http import response`
from rest_framework.response import Response
from rest_framework.views import APIView
from noticias.models import *
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser, MultiPartParser
from noticias.serializers import ComentariosSerializer, NoticiasCreateSerializer, NoticiasViewSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
import math


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
# Create your views here.

#----------- view Comentario ------------------------------#


@permission_classes((AllowAny, ))
class ComentariosView(ListAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'corpo']


@permission_classes((AllowAny, ))
class ComentariosNoticiaView(ListCreateAPIView):

    serializer_class = ComentariosSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        noticia_id = self.kwargs['noticia_id']
        return Comentario.objects.filter(noticia_id__id=noticia_id)


class ComentariosCreateView(ListCreateAPIView):

    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'corpo']

    # def perform_create(self, serializer):
    # serializer.save(autor=self.request.user.id)


@permission_classes((AllowAny, ))
class SingleComentariosView(RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer


@permission_classes((AllowAny, ))
class ComentariosUpdateView(RetrieveUpdateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer

#----------- fim view Comentario ------------------------------#


#----------- view Noticias ------------------------------#

# @permission_classes((AllowAny, ))
# class NoticiasView(ListAPIView):
#     queryset = Noticia.objects.all()
#     serializer_class = NoticiasViewSerializer
#     parser_classes = (MultiPartParser, JSONParser)

#     # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
#     # Para a pesquisa, basta chama essa url com /?search=parametros
#     filter_backends = [SearchFilter]
#     search_fields = ['id', 'titulo', 'corpo', 'autor']


@permission_classes((AllowAny, ))
class NoticiasView(APIView):
    def get(self, request):
        page = int(request.GET.get('page', 1))
        per_page = 10
        noticias = Noticia.objects.all()
        total = noticias.count()
        start = (page - 1) * per_page
        end = page * per_page

        serializer = NoticiasViewSerializer(noticias[start:end], many=True)
        return Response({
            'data': serializer.data,
            'total': total,
            'page': page,
            'last_page': math.ceil(total / per_page)
        })


@permission_classes((AllowAny, ))
class NoticiasCreateView(CreateAPIView):

    queryset = Noticia.objects.all()
    serializer_class = NoticiasCreateSerializer
    #parser_classes = (MultiPartParser, JSONParser)

    # Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    # Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends = [SearchFilter]
    search_fields = ['id', 'titulo', 'corpo', 'autor']


@permission_classes((AllowAny, ))
class SingleNoticiasView(RetrieveAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasViewSerializer


@permission_classes((AllowAny, ))
class NoticiasUpdateView(RetrieveUpdateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasViewSerializer

#----------- fim view Noticias ------------------------------#
