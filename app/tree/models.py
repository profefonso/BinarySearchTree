from django.db import models
from django.contrib.postgres.fields import JSONField


class Tree(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True
    )
    data = JSONField()

    def __str__(self):
        return self.name
