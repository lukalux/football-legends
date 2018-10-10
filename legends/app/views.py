from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from models import Article, Card
from django.shortcuts import render, HttpResponse
from django.db.models import Q

# Create your views here.
# class Home(DetailView):
#     model = Article
#     template_name = 'base.html'
#
#     context = Article.objects.all()
#     print context


def Backup(request):
    articles = Article.objects.all()

    return render(request, 'backup.html', {'articles':articles})


# def Home(request):
#     articles = Article.objects.all()
#
#     return render(request, 'home.html', {'articles':articles})


class Home(ListView):
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    paginate_by = 24
    queryset = Article.objects.all().filter(published=True).order_by('-created_at')


def Search(request):
    q = request.GET['q']
    articles = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q)).filter(published=True)

    context = {
        'search': articles
    }
    return render(request, 'search.html', context)


class Articles(DetailView):
    model = Article
    template_name = 'article.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        article_id = self.kwargs['id']
        context = super(Articles, self).get_context_data(**kwargs)
        context['article'] = Article.objects.filter(id=article_id, published=True)
        context['card'] = Card.objects.filter(card__id=article_id)
        update_count = context['article'].values('counter')[0]['counter'] + 1
        Article.objects.filter(id=article_id).update(counter=update_count)
        return context


# TESTING PURPOSES #
####################
class ArticlesUnpublished(DetailView):
    model = Article
    template_name = 'article_unpublished.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        article_id = self.kwargs['id']
        context = super(ArticlesUnpublished, self).get_context_data(**kwargs)
        context['article'] = Article.objects.filter(id=article_id)
        context['card'] = Card.objects.filter(card__id=article_id)
        return context


