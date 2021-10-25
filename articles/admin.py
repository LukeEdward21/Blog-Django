
from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "thumbnail", "thumbnail_credits", "type", "resume", "author", "created", "updated", "is_exclusive")
    prepopulated_fields = {"slug": ("title",)}
