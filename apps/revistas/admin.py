from django.contrib import admin
from .models import Categoria, Revista, Edicao
from apps.artigos.models import Artigo
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nome_categoria', 'revista')
    list_filter = ('revista',)
    search_fields = ('nome_categoria',)
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'nome_categoria',
    #             'revista'
    #         )
    #     }),
    # )


class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('capa_edicao', 'edicao_portugues', 'artigo_link','data_lancamento', 'revista')
    list_filter = ('revista','data_lancamento')
    list_display_links =('capa_edicao', 'edicao_portugues')
    search_fields = ('nome_categoria','data_lancamento','edicao_portugues','edicao_english')
    readonly_fields = ["capa_edicao"]

    def capa_edicao(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="200px"/>'.format(obj.imagem.url))

    def artigo_link(self, obj):
        print(">>", obj.id)
        count = Artigo.objects.filter(edicao=obj).count()
        url = (
            reverse("admin:artigos_artigo_changelist")
            + "?"
            + urlencode({"edicao__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Artigos</a>', url, count)

    artigo_link.short_description = "Artigos"
    


class RevistaAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'nome_revista_portugues','edicao_link', 'issn')
    list_filter = ()
    list_display_links =('image_tag', 'nome_revista_portugues')
    search_fields = ('nome_revista_portugues','nome_revista_english')

    def image_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="200px"/>'.format(obj.imagem.url))

    def edicao_link(self, obj):
        count = Edicao.objects.filter(revista=obj).count()
        # obj.person_set.count()
        url = (
            reverse("admin:revistas_edicao_changelist")
            + "?"
            + urlencode({"revista__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Edições</a>', url, count)

    edicao_link.short_description = "Ediçoes"


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Edicao, EdicaoAdmin)
admin.site.register(Revista, RevistaAdmin)
