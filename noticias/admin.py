from django.contrib import admin
from .models import Comentario
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'revista_relacionada',
                    'comentatios_link', 'data_postagem']
    list_display_links = ['titulo']
    search_fields = ['data_postagem', 'revista_relacionada',
                     'titulo', 'subtitulo', 'corpo', 'usuario__user']
    list_filter = ['data_postagem', 'revista_relacionada']

    def comentatios_link(self, obj):
        count = Comentario.objects.filter(noticia=obj).count()
        url = (
            reverse("admin:noticias_comentario_changelist")
            + "?"
            + urlencode({"noticia__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Comentário(s)</a>', url, count)

    comentatios_link.short_description = "Comentários"


# admin.site.register(Noticia, NoticiaAdmin)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'noticia', 'data_postagem']
    # list_display_links = ['titulo']
    search_fields = ['corpo', 'noticia', 'data_postagem', 'usuario__user']
    list_filter = ['data_postagem']

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# admin.site.register(Comentario, ComentarioAdmin)
