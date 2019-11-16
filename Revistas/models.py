from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timezone import now

# Create your models here.
class Revista(models.Model):
    
    issn = models.CharField(max_length=20)
    nome_revista_portugues = models.CharField(max_length=100)
    nome_revista_english = models.CharField(max_length=100)
    #imagem = imagem field
    email = models.CharField(max_length=150,blank=True)
    telefone = models.CharField(max_length=25,blank=True)
    local = models.TextField(blank=True)
    sobre = models.TextField(blank=True)
    
    def __str__(self):
        return self.nome_revista_portugues

class Palavras_chave(models.Model):
    
    assunto = models.CharField(max_length=150)
    
    def __str__(self):
        return self.assunto

class Autores(models.Model):

    nome_autor = models.CharField( max_length=150)

    def __str__(self):
        return self.nome_autor

class Edicoes(models.Model):

    edicao_portugues = models.CharField(max_length=100)
    edicao_english = models.CharField(max_length=100)
    data_lancamento = models.DateField()
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=150)
    #imagem = imagem field

   

class Categoria(models.Model):

    
    nome_categoria = models.CharField(max_length=50)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nome_categoria


class Artigos(models.Model):

    
    titulo_portugues = models.CharField( max_length=150)
    titulo_english = models.CharField( max_length=150)
    descricao_portugues = models.TextField(blank=True)
    descricao_english = models.TextField(blank=True)
    autores = models.ManyToManyField(Autores)
    palavras_chave = models.ManyToManyField(Palavras_chave)
    edicao = models.ForeignKey(Edicoes, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=150)
    link_pdf = models.CharField( max_length=200)
   
    

class Usuario(models.Model):
    
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    artigos_favoritos = models.ManyToManyField(Artigos)
    #administrador = models.BooleanField
    
    def __str__(self):
        return self.user




    

class Avaliacoes(models.Model):
    # de 0 a 5 para artigo
    nota =  models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    id_usuario = models.PositiveIntegerField()
    artigo = models.ForeignKey(Artigos, on_delete=models.CASCADE)



class Noticias(models.Model):

    titulo = models.CharField( max_length=150)
    subtitulo = models.CharField(max_length=350, default="Not found")
    corpo  = models.TextField()
    revista_relacionada = models.ForeignKey(Revista, on_delete=models.CASCADE, default=0)
    data_postagem = models.DateTimeField(default=now, editable=False)
    autor = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    link_artigo = models.TextField(blank=True)
    

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):

    corpo = models.TextField()
    autor = models.PositiveIntegerField()
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(default=now, editable=False)
    

