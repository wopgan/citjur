from django.db import models
from django.forms import ValidationError


class BookUp(models.Model):
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255)
    
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

    def validate_file_extension(value):
        if value.file.content_type != 'application/pdf':
            raise ValidationError('Arquivo Inválido')

    upload = models.FileField(upload_to='uploads/', null=False, blank=False, validators=[validate_file_extension])

    def __str__(self):
        return self.titulo


