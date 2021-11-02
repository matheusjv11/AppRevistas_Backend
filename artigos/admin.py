from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import *


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo_portugues', 'revista', 'edicao',
                    'data_lancamento', 'autores_link', 'palavras_chave_link')
    list_filter = ('categoria',)
    list_display_links = ('titulo_portugues',)
    search_fields = ('edicao__edicao_portugues', 'categoria__nome_categoria', 'autores__nome_autor',
                     'palavras_chave__assunto', 'titulo_portugues', 'titulo_english', 'descricao_portugues', 'descricao_english',)

    def data_lancamento(self, obj):
        return obj.edicao.data_lancamento

    def revista(self, obj):
        return obj.edicao.revista

    def autores_link(self, obj):
        count = obj.autores.count()
        url = (
            reverse("admin:artigos_autor_changelist")
            + "?"
            + urlencode({"artigo__id__exact=": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Autores</a>', url, count)

    autores_link.short_description = "Autores"

    def palavras_chave_link(self, obj):
        count = obj.palavras_chave.count()
        url = (
            reverse("admin:artigos_palavrachave_changelist")
            + "?"
            + urlencode({"artigo__id__exact=": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Palavras Chave</a>', url, count)

    palavras_chave_link.short_description = "Palavras Chave"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        revistas_admin = request.user.gerencia_revista.all()
        if request.user.is_superuser:
            return qs
        ids = tuple(list(map(lambda revista: str(revista.pk), revistas_admin)))
        return qs.filter(edicao__revista__in=ids)


admin.site.register(Artigo, ArtigoAdmin)


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome_autor']
    list_display_links = ['nome_autor']
    search_fields = ['nome_autor']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Autor, AutorAdmin)


class PalavraChaveAdmin(admin.ModelAdmin):
    list_display = ['assunto']
    list_display_links = ['assunto']
    search_fields = ['assunto']
    list_filter = []

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(PalavraChave, PalavraChaveAdmin)


# class AvaliacaoAdmin(admin.ModelAdmin):
#     list_display = ['artigo']
#     list_display_links = ['assunto']
#     search_fields = ['assunto']
#     list_filter = []


# admin.site.register(Avaliacao, AvaliacaoAdmin)
