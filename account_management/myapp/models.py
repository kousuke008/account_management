from django.db import models

# Create your models here.
from django.db import models


class User(models.Model):
    kind = models.CharField(max_length=100)  # デフォルト値を指定
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    level = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return self.username