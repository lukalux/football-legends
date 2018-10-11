from __future__ import unicode_literals

from django.db import models
import ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.

class Card(models.Model):
    name = models.CharField(name="name", verbose_name="Player name", max_length=255)
    nickname = models.CharField(name="nickname", verbose_name="Nickname", max_length=255)
    nation = models.CharField(name="nation", verbose_name='nation', max_length=255)
    born = models.DateField()
    clubs = models.TextField(name="clubs", verbose_name='Clubs played', default='')
    appearances = models.IntegerField(name='appearances', verbose_name='Total appeareances')
    goals = models.IntegerField(name='goals', verbose_name='Total goals')
    active_years = models.IntegerField(name='active', verbose_name='Years active', default=0)
    created_at = models.DateField()
    modified_at = models.DateField()
    published = models.BooleanField(name="published", verbose_name="Published", default=False)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"



class Article(models.Model):
    title = models.CharField(name="title", verbose_name="Title", max_length=255)
    slug = models.SlugField(name="slug", unique=True)
    card = models.ForeignKey(Card, related_name='card', verbose_name='Player Card', default='')
    photo = models.ImageField(upload_to="uploads/headers", blank=True)
    content = RichTextUploadingField(name="content", verbose_name="content", blank=True)
    counter = models.IntegerField(name="counter", verbose_name='Number of openings', default=0, blank=False)
    created_at = models.DateField()
    modified_at = models.DateField()
    published = models.BooleanField(name="published", verbose_name="Published", default=False)

    def __unicode__(self):
        return "%s" % self.title

    # NEEDED FOR SITEMAP GENERATOR #
    ################################
    def get_absolute_url(self):
        return "/articles/%i/" % self.id
    ################################

    def save(self, *args, **kwargs):
        if self.photo:
            image = Image.open(StringIO.StringIO(self.photo.read()))
            if image.mode != 'RGB':
                image = image.convert('RGB')
            if self.photo.width >= self.photo.height:
                new_width = 800
                image.thumbnail((new_width, new_width * self.photo.height / self.photo.width), Image.ANTIALIAS)
            else:
                new_width = 500
                image.thumbnail((new_width, new_width * self.photo.height / self.photo.width), Image.ANTIALIAS)
            output = StringIO.StringIO()
            image.save(output, format='JPEG', quality=50)
            output.seek(0)
            self.photo = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.photo.name.split(".")[0],'image/jpeg', output.len, None)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


