from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name of good')
    content = models.TextField(null=True, blank=True, verbose_name='Some description')
    price = models.FloatField(null=True, blank=True, verbose_name='Price')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Date of published')
    theme = models.ForeignKey('Theme', null=True, on_delete=models.PROTECT, verbose_name='Theme')

    class Meta:
        verbose_name_plural = 'Goods'
        verbose_name = 'Good'
        ordering = ['-published']


class Theme(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Theme name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Themes'
        verbose_name = 'Theme'
        ordering = ('name',)