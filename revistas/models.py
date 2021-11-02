from django.db import models
from django.conf import settings
from django.utils.html import mark_safe


class Revista(models.Model):
    # Informações sobre cada revista registrada

    issn = models.CharField(max_length=20)
    oai_url = models.CharField(max_length=100, blank=True)
    nome_revista_portugues = models.CharField(max_length=100)
    nome_revista_english = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    email = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=25, blank=True)
    local = models.TextField(blank=True)
    sobre = models.TextField(blank=True)

    def __str__(self):
        return self.nome_revista_portugues


class Categoria(models.Model):
    # Informação sobre as categorias que as revistas usam

    nome_categoria = models.CharField(max_length=50)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_categoria


class Edicao(models.Model):
    # Informações das edições de cada revista
    edicao_portugues = models.CharField(max_length=100)
    edicao_english = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)

    class Meta:
        # Manter Ediçõe - django adiciona o 's' no fim
        verbose_name = 'Ediçõe'

    def __str__(self):
        return self.edicao_portugues
