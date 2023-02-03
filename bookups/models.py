from django.db import models
from django.core.validators import FileExtensionValidator


class Book(models.Model):

    class Meta:
        verbose_name = '1 - Livro'
        verbose_name_plural = '1 - Livros'

    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100, verbose_name='Autor')
    title = models.CharField(max_length=100, verbose_name='Título')
    publisher = models.CharField(null=True, blank=False, max_length=100, verbose_name='Editora')
    publisher_website = models.URLField(null=True, blank=False, verbose_name='Site da Editora')
    
    period_in_school = [
        ('1', 'Primeiro Semestre'),  
        ('2', 'Segundo Semestre'),
        ('3', 'Terceiro Semestre'),
        ('4', 'Quarto Semestre'),
        ('5', 'Quinto Semestre'),
        ('6', 'Sexto Semestre'),
        ('7', 'Setimo Semestre'),
        ('8', 'Quinto Semestre'),
        ('9', 'Quinto Semestre'),
        ('10', 'Quinto Semestre'),
    ]

    period = models.CharField(max_length=2, choices=period_in_school, verbose_name='Período' )
    book = models.FileField(upload_to='uploads/', null=True, blank=False, validators=[FileExtensionValidator(['pdf'])], verbose_name='Upload do Livro')

    def __str__(self):
        return f"{self.title}, de {self.author}"


class InfoBook(models.Model):

    class Meta:
        verbose_name = '2 - Descrição do livro'
        verbose_name_plural = '2 - Descrições dos Livros'

    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return f'Descrição - {self.id} - {self.book.title}'

class Finder(models.Model):

    class Meta:
        verbose_name = '3 - Pesquisa'
        verbose_name_plural = '3 - Pesquisas'

    id = models.AutoField(primary_key=True)
    infobook = models.ForeignKey(InfoBook, on_delete=models.CASCADE)
    #book = models.ForeignKey(Book, on_delete=True)
    find = models.CharField(max_length=100, verbose_name='Pesquisa')

    def __str__(self):
        return f'Pesquisa - tag #{self.find} - {self.infobook.book}'
