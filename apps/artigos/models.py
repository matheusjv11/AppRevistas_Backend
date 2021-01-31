from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PalavraChave(models.Model):
    class Meta:
        verbose_name = 'Palavras chave'
    # Palavras-chaves que vêm em cada artigo
    assunto = models.CharField(max_length=150)

    def __str__(self):
        return self.assunto


class Autor(models.Model):
    class Meta:
        verbose_name = 'Autore'
    # Autores dos artigos (Um autor pode estar em varios artigos)
    nome_autor = models.CharField(max_length=150)

    def __str__(self):
        return self.nome_autor


class Artigo(models.Model):
    # Todos os dados dos artigos recolhidos

    titulo_portugues = models.CharField(max_length=150)
    titulo_english = models.CharField(max_length=150)
    descricao_portugues = models.TextField(blank=True)
    descricao_english = models.TextField(blank=True)
    autores = models.ManyToManyField(Autor)
    palavras_chave = models.ManyToManyField(PalavraChave)
    edicao = models.ForeignKey("revistas.Edicao", on_delete=models.CASCADE)
    categoria = models.ForeignKey("revistas.Categoria", on_delete=models.CASCADE)
    identifier = models.CharField(max_length=150)
    link_pdf = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo_portugues
    
    def revista(self):
        return self.edicao.revista


class Avaliacao(models.Model):

    class Meta:
        verbose_name = 'Avaliaçõe'
    # Avaliação que será relacionado aos artigos
    # de 0 a 5 para artigo
    nota = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE, default=None)
    artigo = models.ForeignKey("artigos.Artigo", on_delete=models.CASCADE, default=None)
    
