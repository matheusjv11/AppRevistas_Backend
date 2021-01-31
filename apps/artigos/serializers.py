from apps.revistas.serializers import CategoriaSerializer
from apps.artigos.models import *
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


class AutoresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Autor
        fields = ('id', 'nome_autor')


class PalavrasChaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PalavraChave
        fields = ('id', 'assunto')


class ArtigosSerializer(serializers.ModelSerializer):

    autores = AutoresSerializer(many=True, read_only=True)
    palavras_chave = PalavrasChaveSerializer(many=True, read_only=True)
    categoria = CategoriaSerializer(many=False, read_only=True)

    class Meta:
        model = Artigo
        #fields = ('id', 'titulo_portugues', 'titulo_english', 'descricao_portugues', 'descricao_english', 'link_pdf','categoria','edicao','autores__id')
        fields = '__all__'


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'nota', 'usuario', 'artigo')


class ArtigosParaUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artigo
        fields = ['id']
