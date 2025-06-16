from django.db import models

class Edicao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.URLField()  
    publicado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
