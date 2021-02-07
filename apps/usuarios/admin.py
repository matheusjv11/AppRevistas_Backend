from apps.usuarios.models import Usuario
from django.contrib import admin

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('email', 'first_name')
    list_filter = ()
    list_display_links =('email',)
    search_fields = ('email', 'first_name')



admin.site.register(Usuario, UsuarioAdmin)