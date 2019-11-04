from django.contrib import admin
from .models import Usuario, Categoria, Revista, Edicoes, Artigos, Autores,  Palavras_chave

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Revista)
admin.site.register(Edicoes)
admin.site.register(Artigos)
admin.site.register(Autores)
admin.site.register(Palavras_chave)
# Register your models here.
