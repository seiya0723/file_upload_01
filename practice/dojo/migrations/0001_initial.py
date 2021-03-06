# Generated by Django 3.2.9 on 2022-01-08 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日')),
                ('content', models.FileField(upload_to='dojo/document/content', verbose_name='ファイル')),
            ],
        ),
    ]
