from django.db import models


class Document(models.Model):
    imagen = models.FileField(upload_to='media')
