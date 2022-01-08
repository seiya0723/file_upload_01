from django.db import models
from django.utils import timezone

class Document(models.Model):

    dt = models.DateTimeField(verbose_name="投稿日", default=timezone.now)
    name = models.CharField(verbose_name="ファイル名", max_length=500)
    content   = models.FileField(verbose_name="ファイル", upload_to="dojo/document/content")

    mime = models.TextField(verbose_name="MIMEタイプ",null=True,blank=True)

    def __str__(self):
        return self.comment
