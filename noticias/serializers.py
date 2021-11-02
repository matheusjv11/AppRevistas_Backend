from noticias.models import *
from revistas.serializers import Base64ImageField, RevistaSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


#from drf_extra_fields.fields import Base64ImageField
#from django_rest_framework_base64_fields import Base64FileField

User = get_user_model()


class NoticiasCreateSerializer(serializers.ModelSerializer):
    #revista_relacionada = RevistaSerializer(many=False, read_only=True)
    imagem = Base64ImageField()

    class Meta:
        model = Noticia
        fields = ('id', 'titulo', 'subtitulo', 'corpo', 'data_postagem', 'id_autor',
                  'nome_autor', 'revista_relacionada', 'link_artigo', 'imagem')
        extra_kwargs = {
            'id_autor': {'read_only': False},
            'nome_autor': {'read_only': True},
        }

    def create(self, validated_data):

        titulo = validated_data['titulo']
        subtitulo = validated_data['subtitulo']
        corpo = validated_data['corpo']
        id_autor = validated_data['id_autor']
        revista_relacionada = validated_data['revista_relacionada']
        link_artigo = validated_data['link_artigo']
        imagem = validated_data['imagem']
        user = User.objects.get(id=id_autor)
        first_name = user.first_name
        last_name = user.last_name
        nome_completo = first_name+" "+last_name

        noticias_obj = Noticia(titulo=titulo, subtitulo=subtitulo, corpo=corpo, id_autor=id_autor,
                               nome_autor=nome_completo, revista_relacionada=revista_relacionada, link_artigo=link_artigo, imagem=imagem)
        noticias_obj.save()

        return validated_data


class NoticiasViewSerializer(serializers.ModelSerializer):
    revista_relacionada = RevistaSerializer(many=False, read_only=True)
    imagem = Base64ImageField()

    class Meta:
        model = Noticia
        fields = ('visivel', 'id', 'titulo', 'subtitulo', 'corpo', 'data_postagem', 'usuario',
                  'nome_autor', 'revista_relacionada', 'link_artigo', 'imagem')

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'


class ComentariosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comentario
        fields = ('id', 'corpo', 'nome_autor',
                  'noticia', 'data_postagem', )
        extra_kwargs = {
            'id_autor': {'read_only': False},
            'nome_autor': {'read_only': True, 'write_only': False},
            'data_postagem': {'read_only': True, 'write_only': False},
        }

    def create(self, validated_data):

        corpo = validated_data['corpo']
        id_autor = validated_data['id_autor']
        noticia = validated_data['noticia']

        user = User.objects.get(id=id_autor)
        first_name = user.first_name
        last_name = user.last_name
        nome_completo = first_name+" "+last_name

        comentario_obj = Comentario(
            corpo=corpo, id_autor=id_autor, nome_autor=nome_completo, noticia=noticia)
        comentario_obj.save()

        return validated_data
