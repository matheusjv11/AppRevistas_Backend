from rest_framework import serializers
from rest_framework.serializers import CharField, EmailField
from rest_framework.validators import ValidationError
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Revistas.models import Autores, Artigos,Categoria,Edicoes,Revista, Palavras_chave,Noticias,Comentarios, Usuario, Avaliacoes
from django.db.models import Q
from django.core.files.base import ContentFile
import base64

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self,data):

        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Email já registrado ! tente novamente.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(serializers.ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label="Email adress",required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','token')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self,data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data['password']

        if not email and not username:
            raise ValidationError("É necessario um email ou username para efetuar o login")

        user = User.objects.filter(
            Q(email=email)|
            Q(username=username)
        ).distinct()
        

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("Esse email ou username não é valido")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Credenciais invalidas")
        
        data['TOKEN'] = 'SOME RANDOM TOKEN'
        return data

class RevistaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Revista
        fields = ('id', 'issn', 'nome_revista_portugues', 'nome_revista_english')

class AutoresSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Autores
        fields = ('id', 'nome_autor')

class PalavrasChaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Palavras_chave
        fields = ('id', 'assunto')


class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('id', 'nome_categoria', 'revista_id')

class ArtigosSerializer(serializers.ModelSerializer):
    
    autores = AutoresSerializer(many=True, read_only=True)
    palavras_chave = PalavrasChaveSerializer(many=True, read_only=True)
    categoria = CategoriaSerializer(many=False, read_only=True)
    
    class Meta:
        model = Artigos
        #fields = ('id', 'titulo_portugues', 'titulo_english', 'descricao_portugues', 'descricao_english', 'link_pdf','categoria','edicao','autores__id')
        fields = '__all__'



class EdicoesSerializer(serializers.ModelSerializer):

    revista_id = RevistaSerializer
    class Meta:
        model = Edicoes
        fields = ('id', 'edicao_portugues', 'edicao_english', 'data_lancamento','revista_id')
   

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('id', 'nota', 'id_usuario', 'artigo_id')

"""class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
"""
class Base64ImageField(serializers.ImageField):
    def from_native(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super(Base64ImageField, self).from_native(data)

class NoticiasSerializer(serializers.ModelSerializer):
    imagem = Base64ImageField(allow_null=True)
    class Meta:
        model = Noticias
        fields = ('id', 'titulo', 'subtitulo','corpo','data_postagem','autor','revista_relacionada', 'link_artigo','imagem')
        extra_kwargs = {
            'autor': {'read_only': True},
        }



class ComentariosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comentarios
        fields = ('id', 'corpo','autor','noticia')
        extra_kwargs = {
            'autor': {'read_only': True},
        }

