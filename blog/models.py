from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=20, default='User')
    image = models.ImageField(upload_to='static')
    title = models.CharField(max_length=50, null=True, blank=True)
    desc = models.TextField(max_length=150)

    def __str__(self):
        return f"Автор:{self.author}, Пост: {self.title}"

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

