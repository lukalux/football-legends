from django.contrib import admin
from models import Article, Card

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'counter', 'published', 'created_at', 'modified_at')
    prepopulated_fields = {'slug': ('title',)}


class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'nation', 'created_at', 'modified_at')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Card, CardAdmin)