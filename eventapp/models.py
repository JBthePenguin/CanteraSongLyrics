from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='titre')
    description = models.TextField(verbose_name='description')
    start_time = models.DateTimeField(verbose_name='date de début')
    end_time = models.DateTimeField(
        null=True, blank=True, default=None, verbose_name='date de fin')

    class Meta:
        verbose_name = "Évènement"
        verbose_name_plural = "Évènements"
