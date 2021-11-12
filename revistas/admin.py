from django.contrib import admin
from artigos.models import Artigo
from revistas.management.commands.scriptsTest import run
from .models import Categoria, Revista, Edicao
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django.contrib import messages


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nome_categoria', 'revista')
    list_filter = ('revista',)
    search_fields = ('nome_categoria',)

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Categoria, CategoriaAdmin)


class EdicaoAdmin(admin.ModelAdmin):
    list_display = ('capa_edicao', 'edicao_portugues',
                    'artigo_link', 'data_lancamento', 'revista')
    list_filter = ('revista', 'data_lancamento')
    list_display_links = ('capa_edicao', 'edicao_portugues')
    search_fields = ('nome_categoria', 'data_lancamento',
                     'edicao_portugues', 'edicao_english')
    readonly_fields = ["capa_edicao"]

    def capa_edicao(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="200px"/>'.format(obj.imagem.url))

    def artigo_link(self, obj):
        count = Artigo.objects.filter(edicao=obj).count()
        url = (
            reverse("admin:artigos_artigo_changelist")
            + "?"
            + urlencode({"edicao__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Artigos</a>', url, count)

    artigo_link.short_description = "Artigos"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        revistas_admin = request.user.gerencia_revista.all()
        if request.user.is_superuser:
            return qs
        ids = tuple(list(map(lambda revista: str(revista.pk), revistas_admin)))
        return qs.filter(revista__in=ids)


admin.site.register(Edicao, EdicaoAdmin)


class RevistaAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'nome_revista_portugues',
                    'edicao_link', 'issn')
    list_filter = ()
    list_display_links = ('image_tag', 'nome_revista_portugues')
    search_fields = ('nome_revista_portugues', 'nome_revista_english')

    def image_tag(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="200px"/>'.format(obj.imagem.url))

    def edicao_link(self, obj):
        count = Edicao.objects.filter(revista=obj).count()
        url = (
            reverse("admin:revistas_edicao_changelist")
            + "?"
            + urlencode({"revista__id__exact": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Edições</a>', url, count)

    edicao_link.short_description = "Ediçoes"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        revistas_admin = request.user.gerencia_revista.all()
        if request.user.is_superuser:
            return qs
        ids = tuple(list(map(lambda revista: str(revista.pk), revistas_admin)))
        return qs.filter(id__in=ids)

    actions = ['make_published']

    @admin.action(description='Atualizar dados da revista')
    def make_published(self, request, queryset):
        print(queryset)

        for revista in queryset:
            if(revista.oai_url):
                print(revista.oai_url)
                run(revista.oai_url)
            else:
                print(revista.nome_revista_portugues)

            # messages.error(request, "The message" +
            #                revista.nome_revista_portugues)

        # queryset.update(status='p')


admin.site.register(Revista, RevistaAdmin)
