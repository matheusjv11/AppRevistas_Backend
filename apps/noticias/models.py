from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Noticia(models.Model):

    class Meta:
        verbose_name = 'Notícia'

    # Noticias da página inicial do APP
    visivel = models.BooleanField(default=True)
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=350, default="Not found")
    corpo = models.TextField()
    revista_relacionada = models.ForeignKey(
        "revistas.Revista", on_delete=models.CASCADE, default=0)
    data_postagem = models.DateTimeField(default=now, editable=False)
    usuario = models.ForeignKey(
        'usuarios.Usuario', default=None, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    link_artigo = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

    def revista_str(self):
        return self.revista_relacionada
        
    @property
    def nome_autor(self):
        return self.usuario.username


class Comentario(models.Model):

    class Meta:
        verbose_name = 'Comentário'

    # Comentarios de cada noticia
    visivel = models.BooleanField(default=True, verbose_name='Visível')
    corpo = models.TextField(verbose_name='Corpo do comentário')
    usuario = models.ForeignKey(
        'usuarios.Usuario', default=None, on_delete=models.CASCADE, verbose_name='Usuário')
    noticia = models.ForeignKey(
        "noticias.Noticia", on_delete=models.CASCADE, verbose_name='Notícia')
    data_postagem = models.DateTimeField(
        default=now, editable=False, verbose_name='Data de postagem')
