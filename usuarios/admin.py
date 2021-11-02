from usuarios.managers import AccountManager
from usuarios.models import Usuario
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.site_header = "Sistema de Administração de Revistas"
admin.site.site_title = "Sistema de Administração de Revistas"
# admin.site.index_title = "Index title"


class UserAdminConfig(UserAdmin):
    list_display = ['email', 'username', 'first_name']
    search_fields = ['email', 'username', 'city']
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informaçoes pessoais', {
         'fields': ('username', 'first_name', 'last_name', 'date_of_birth', 'city')}),
        ('Atividades', {'fields': ('date_joined', 'last_login')}),
        ('Permisões', {'fields': ('is_admin',
                                  'is_active', 'is_staff', 'is_superuser', 'gerencia_revista', 'groups', 'user_permissions')}),
        ('Artigos', {'fields': ('artigos_favoritos',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'date_of_birth', 'city', 'password1', 'password2'),
        }),
    )

    # def get_queryset(self, request):
    #     # qs = super(UserAdminConfig, self).get_queryset(request)
    #     # return qs.filter()
    #     print(request.user.username)
    #     return Usuario.objects.all()

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(author=request.user)


admin.site.register(Usuario, UserAdminConfig)


# class UsuarioAdmin(admin.ModelAdmin):

#     list_display = ('email', 'first_name')
#     # list_filter = ()
#     # list_display_links = ('email',)
#     # search_fields = ('email', 'first_name')
#     # add_fieldsets = (
#     #     (None, {
#     #         'classes': ('wide',),
#     #         'fields': ('email', 'password1', 'password2'), }),)


# admin.site.register(Usuario, UsuarioAdmin)
