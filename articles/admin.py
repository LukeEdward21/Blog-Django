
from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "thumbnail", "resume", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
