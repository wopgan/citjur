from django.core.validators import FileExtensionValidator
from django.db import models

class BookUp(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255)
    editora = models.CharField(null=True, blank=False, max_length=255)
    site_editora = models.CharField(null=True, blank=False, max_length=255)
    
    period_in_school = [
       ('1', 'Primeiro Período'),
       ('2', 'Segundo Período'),
       ('3', 'Terceiro Período'),
       ('4', 'Quarto Período'),
       ('5', 'Quinto Período'),
    ]

    periodo = models.CharField(max_length=1, choices = period_in_school)
    descricao = models.TextField()
    pesquisa = models.TextField()

    upload = models.FileField(upload_to='uploads/',null=True, blank=False, validators=[FileExtensionValidator( ['pdf'] ) ])

    def __str__(self):
        return self.titulo


