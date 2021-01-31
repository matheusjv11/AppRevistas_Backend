from apps.noticias.models import *
from rest_framework.filters import SearchFilter
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.noticias.serializers import ComentariosSerializer, NoticiasCreateSerializer, NoticiasViewSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

# Create your views here.

#----------- view Comentario ------------------------------#

@permission_classes((AllowAny, ))
class ComentariosView(ListAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentariosSerializer

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','corpo']
    
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

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','corpo']

    #def perform_create(self, serializer):
        #serializer.save(autor=self.request.user.id)

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

@permission_classes((AllowAny, ))
class NoticiasView(ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasViewSerializer
    parser_classes = (MultiPartParser, JSONParser)

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo','corpo','autor']


@permission_classes((AllowAny, ))
class NoticiasCreateView(CreateAPIView):
    
    queryset = Noticia.objects.all()
    serializer_class = NoticiasCreateSerializer
    #parser_classes = (MultiPartParser, JSONParser)

    #Essa parte indica que a pode ser retornado só os dados pesquisados por esses parametros
    #Para a pesquisa, basta chama essa url com /?search=parametros
    filter_backends=[SearchFilter]
    search_fields = ['id','titulo','corpo','autor']


@permission_classes((AllowAny, ))
class SingleNoticiasView(RetrieveAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasViewSerializer


@permission_classes((AllowAny, ))
class NoticiasUpdateView(RetrieveUpdateAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiasViewSerializer

#----------- fim view Noticias ------------------------------#