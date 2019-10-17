from django.db import models


class Song(models.Model):
    title = models.CharField(
        db_index=True, unique=True, max_length=255,
        error_messages={
            'unique': 'Une chanson avec ce titre est déjà répertoriée'
        })
    lyrics = models.TextField()
