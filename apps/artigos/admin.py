from django.contrib import admin
from .models import *


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo_portugues', 'revista','edicao', 'categoria', 'data_lancamento')
    list_filter = ('categoria',)
    list_display_links = ('titulo_portugues',)
    search_fields = ('edicao__edicao_portugues', 'categoria__nome_categoria', 'autores__nome_autor',
                     'palavras_chave__assunto', 'titulo_portugues', 'titulo_english', 'descricao_portugues', 'descricao_english',)

    def data_lancamento(self, obj):
        return obj.edicao.data_lancamento
    
    def revista(self, obj):
        return obj.edicao.revista


admin.site.register(Artigo, ArtigoAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome_autor']
    list_display_links = ['nome_autor']
    search_fields = ['nome_autor']


admin.site.register(Autor, AutorAdmin)


class PalavraChaveAdmin(admin.ModelAdmin):
    list_display = ['assunto']
    list_display_links = ['assunto']
    search_fields = ['assunto']
    list_filter = []


admin.site.register(PalavraChave, PalavraChaveAdmin)


# class AvaliacaoAdmin(admin.ModelAdmin):
#     list_display = ['artigo']
#     list_display_links = ['assunto']
#     search_fields = ['assunto']
#     list_filter = []

# admin.site.register(Avaliacao, AvaliacaoAdmin)
