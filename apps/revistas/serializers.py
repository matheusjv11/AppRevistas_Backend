from apps.revistas.models import Categoria, Edicao, Revista
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


class Base64ImageField(serializers.ImageField):
    def from_native(self, data):
        if isinstance(data, basestring) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super(Base64ImageField, self).from_native(data)


class RevistaSerializer(serializers.ModelSerializer):
    imagem = Base64ImageField()

    class Meta:
        model = Revista
        fields = '__all__'


class EdicoesSerializer(serializers.ModelSerializer):
    imagem = Base64ImageField()
    revista_id = RevistaSerializer

    class Meta:
        model = Edicao
        fields = ('id', 'edicao_portugues', 'edicao_english',
                  'data_lancamento', 'revista_id', 'imagem')


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nome_categoria', 'revista_id')

