from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name of good')
    content = models.TextField(null=True, blank=True, verbose_name='Some description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date of published')

    class Meta:
        verbose_name_plural = 'Goods'
        verbose_name = 'Good'
        ordering = ['-published']