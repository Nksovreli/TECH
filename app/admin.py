from django.contrib import admin
from .models import Article, ArticleBlock

class ArticleBlockInline(admin.TabularInline):
    model = ArticleBlock
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleBlockInline]