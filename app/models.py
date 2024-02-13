from django.db import models
from ordered_model.models import OrderedModel
from content.models import Category
from content.models import Article

class Menu(OrderedModel):
    name = models.CharField(max_length=250)
    link = models.URLField()
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Block(OrderedModel):
    ARTICLE_CHOICES = [
        ('standard', 'Standard'),
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ]

    link_and_rearrange = models.ManyToManyField(Article, blank=True)
    visual_selection = models.CharField(max_length=20, choices=ARTICLE_CHOICES)
    position = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title




class Article(models.Model):
    blocks = models.ManyToManyField(Block, through='ArticleBlock')


class ArticleBlock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    position = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['position']