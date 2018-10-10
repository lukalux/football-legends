from django import template
from django.shortcuts import render
from django import template

from legends.app.models import Article

register = template.Library()

@register.inclusion_tag('popular.html')
def popular():
    popular = Article.objects.all().filter(published=True).order_by('-counter')

    context = {
        'popular': popular
    }

    return context