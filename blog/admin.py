from blog.models import Post
from django.contrib import admin


# тут отображаем данные из модели в админке

class PostAdmin(admin.ModelAdmin):
    list_display = ("image", "title", "desc")
    search_fields = ["title"]


admin.site.register(Post, PostAdmin)
