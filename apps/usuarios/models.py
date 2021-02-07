from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager

# Create your models here.


class Usuario(AbstractUser):
    
    class Meta:
        verbose_name = 'Usuário'

    # username = None
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    artigos_favoritos = models.ManyToManyField("artigos.Artigo",blank=True)
    administrador = models.BooleanField(default=False)
    gerencia_revista = models.ManyToManyField("revistas.Revista", blank=True)
    
    def __str__(self):
        return self.email

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
