from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categoria(Base):
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.descricao


class Produto(Base):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


class Avaliacao(Base):
    produto = models.ForeignKey(Produto, related_name="avaliacoes",
                                on_delete=models.CASCADE, blank=True)
    avaliador = models.CharField(max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    nota = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        ordering = ['id']
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'produto']

    def __str__(self):
        return f'Avaliador:{self.avaliador}, Produto: {self.produto}, Nota: {self.nota}'
