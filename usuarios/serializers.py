from usuarios.models import *
from artigos.serializers import ArtigosParaUsuarioSerializer, ArtigosSerializer
from rest_framework import serializers
from rest_framework.serializers import CharField, EmailField
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.files.base import ContentFile
from rest_framework.authtoken.models import Token
import base64
#from drf_extra_fields.fields import Base64ImageField
#from django_rest_framework_base64_fields import Base64FileField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'first_name',
                  'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):

        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("Email já registrado ! tente novamente.")
        return data

    def create(self, validated_data):
        username = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = Usuario(username=username, first_name=first_name,
                        last_name=last_name, email=email)
        user_obj.set_password(password)
        user_obj.save()

        # Cria token e um usuario especifico da aplicação
        Token.objects.get_or_create(user=user_obj)
        # usuario = Usuario(user=user_obj)
        # usuario.save()
        return validated_data


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')
        extra_kwargs = {
            'username': {'read_only': True},
        }


class UserLoginSerializer(serializers.ModelSerializer):

    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label="Email adress", required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'token')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data['password']

        if not email and not username:
            raise ValidationError(
                "É necessario um email ou username para efetuar o login")

        user = User.objects.filter(
            Q(email=email) |
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

class AuthUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "_all_"


class UsuarioAppSerializer(serializers.ModelSerializer):

    artigos_favoritos = ArtigosSerializer(many=True, read_only=True)
    # current_user = serializers.SerializerMethodField('_user')
    
    @property
    def _user(self, obj):
        request = self.context.get('request', None)
        if request:
            return AuthUserSerializer(request.user)
     
    class Meta:
        model = Usuario
        fields =  ('administrador', 'artigos_favoritos', 'auth_token', 'email', 'first_name', 'gerencia_revista', 'groups', 'id', 'last_name',)
        extra_kwargs = {
            'administrador': {'read_only': True},
        }
