# Generated by Django 4.0 on 2022-10-25 00:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_bookup_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookup',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
