from rest_framework import serializers
from rest_framework.serializers import CharField, EmailField
from rest_framework.validators import ValidationError
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Revistas.models import Autores, Artigos,Categoria,Edicoes,Revista, Palavras_chave,Noticias,Comentarios
from django.db.models import Q


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

class ArtigosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Artigos
        #fields = ('id', 'titulo_portugues', 'titulo_english', 'descricao_portugues', 'descricao_english', 'link_pdf','categoria','edicao','autores__id')
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categoria
        fields = ('id', 'nome_categoria', 'revista_id')

class EdicoesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Edicoes
        fields = ('id', 'edicao_portugues', 'edicao_english', 'data_lancamento','revista_id')

class PalavrasChaveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Palavras_chave
        fields = ('id', 'assunto')

class NoticiasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticias
        fields = ('id', 'titulo', 'corpo','data_postagem','autor','artigo_relacionado')
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
