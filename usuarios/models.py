from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, User
from .managers import CustomUserManager, AccountManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # date_of_birth = models.DateField(
    #     verbose_name='date of birth', null=True, blank=True)
    # city = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(
        verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    artigos_favoritos = models.ManyToManyField("artigos.Artigo", blank=True)
    administrador = models.BooleanField(default=False)
    gerencia_revista = models.ManyToManyField("revistas.Revista", blank=True)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    def __str__(self):
        return self.email

    @property
    def nome(self):
        return self.username

# class AccountManager(BaseUserManager):
#     def create_user(self,email,username,first_name,password,**other_fields):
#         if not email:
#             raise ValueError(_("Users must have an email address"))
#         if not username:
#             raise ValueError(_("Users must have an unique username"))
#         email=self.normalize_email(email)
#         user=self.model(email=email,username=username,first_name=first_name,**other_fields)
#         user.set_password(password)
#         user.save()

#     def create_superuser(self,email,username,first_name,password,**other_fields):
#             other_fields.setdefault('is_staff',True)
#             other_fields.setdefault('is_superuser',True)
#             other_fields.setdefault('is_active',True)
#             if other_fields.get('is_staff') is not True:
#                 raise ValueError('is_staff is set to False')
#             if other_fields.get('is_superuser') is not True:
#                 raise ValueError('is_superuser is set to False')
#             return self.create_user(email,username,first_name,password,**other_fields)


# class Usuario(User):

#     class Meta:
#         verbose_name = 'Usuário'

#     # username = None
#     # email = models.EmailField(('email address'), unique=True)
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = []

#     # objects = CustomUserManager()

#     artigos_favoritos = models.ManyToManyField("artigos.Artigo", blank=True)
#     administrador = models.BooleanField(default=False)
#     gerencia_revista = models.ManyToManyField("revistas.Revista", blank=True)

    # def __str__(self):
    #     return self.email

    # @property
    # def nome(self):
    #     return self.user.username

# class Usuario(models.Model):

#     class Meta:
#         verbose_name = 'Usuário'

#     # Usuario do APP
#     user = models.OneToOneField(
#         User, related_name='profile', on_delete=models.CASCADE)
#     artigos_favoritos = models.ManyToManyField("artigos.Artigo")
#     administrador = models.BooleanField(default=False)
#     gerencia_revista = models.ManyToManyField("revistas.Revista")

#     def __str__(self):
#         return self.user.username

#     @property
#     def nome(self):
#         return self.user.username

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Usuario.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
