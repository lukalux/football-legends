"""legends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from app.views import Home, Backup, Search, Articles, ArticlesUnpublished
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.flatpages import views as flat_views
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import ArticleSitemap
#
#
sitemaps = {
    'articles': ArticleSitemap
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^search/$', views.Search, name='search'),
    url(r'^articles/(?P<id>[\d-]+)/$', Articles.as_view(), name='articles'),
    # url(r'^backup/$', views.Backup, name='backup'),
    url(r'^unpublished/articles/(?P<id>[\d-]+)/$', ArticlesUnpublished.as_view(), name='articles-unpublished'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
