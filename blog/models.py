from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    updated = models.DateTimeField(auto_now=True, verbose_name="обновлено")
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="слаг")
    title = models.CharField(max_length=100, blank=True, default='', verbose_name="заголовок")
    description = models.TextField(blank=True, verbose_name="описание")
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name='post_author', verbose_name="автор" )
    available = models.BooleanField(default=True, verbose_name="доступно")

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title   
    def get_absolute_url(self):
        return "post/%s/" %(self.slug)

