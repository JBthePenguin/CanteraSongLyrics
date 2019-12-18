from django.db import models


class Song(models.Model):
    title = models.CharField(
        db_index=True, unique=True, max_length=255, verbose_name='titre',
        error_messages={
            'unique': 'Un chant avec ce titre est déjà répertoriée'
        })
    author = models.CharField(
        db_index=True, max_length=255, verbose_name='auteur',
        default="", blank=True)
    lyrics = models.TextField(verbose_name='paroles')

    class Meta:
        ordering = ['title']
        verbose_name = "Chant"
        verbose_name_plural = "Chants"
