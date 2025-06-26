from django.db import models

class Destaques(models.Model):
    imagem = models.URLField()
   #FUturamente adicionar aqui o link de redirecionamento da imagem, que será um destaque de alguma edição do jornal
    ordem = models.IntegerField(default=0)

    def __str__(self):
        return f"Imagem {self.id}"
    
class Outros_grupos(models.Model):
    imagem = models.URLField()
    descricao = models.TextField()
    ordem = models.IntegerField(default=0)

    def __str__(self):
        return f"Imagem {self.id}"
    
class Edicao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.URLField()  
    publicado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

