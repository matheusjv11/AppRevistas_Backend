from revistas.models import Revista
from artigos.models import Artigo
from usuarios.models import Usuario
from rest_framework.filters import SearchFilter
from usuarios.serializers import UserSerializer, UserUpdateSerializer, UsuarioAppSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class BaseManageView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)
        return Response(status=405)



#------ views de Usuarios ------------------------#

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

@permission_classes((AllowAny, ))
class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

#------ fim de Usuarios ------------------------#


#----------- view Usuario APP ------------------------------#

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
        # user_id = self.kwargs['user_id']
        return Usuario.objects.filter(id=self.request.user.id)

@permission_classes((AllowAny, ))
class UsuarioAppAddFavsView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        artigo_id = self.kwargs.get('artigo_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        artigo_OBJ  = Artigo.objects.get(id=artigo_id)


        usuario_OBJ.artigos_favoritos.add(artigo_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)
    
class UsuarioAppRemoveFavsView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):

        usuario_id = self.kwargs.get('user_id')
        artigo_id = self.kwargs.get('artigo_id')

        usuario_OBJ = Usuario.objects.get(id=usuario_id)
        artigo_OBJ  = Artigo.objects.get(id=artigo_id)


        usuario_OBJ.artigos_favoritos.remove(artigo_OBJ)
        
        return Usuario.objects.filter(id=usuario_id)


@permission_classes((AllowAny, ))
class UsuarioAppAddAdminView(ListAPIView):

    serializer_class = UsuarioAppSerializer
    
    def get_queryset(self):
        #trocar isso pra pegar por id do usuario django

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

#----------- fim view Usuario APP ------------------------------#
