# Generated by Django 3.2.10 on 2022-01-08 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0002_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='mime',
            field=models.TextField(blank=True, null=True, verbose_name='MIMEタイプ'),
        ),
    ]
