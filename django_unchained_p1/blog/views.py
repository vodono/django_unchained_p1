from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Article, Tag
from django.db.models import Count


def index(request):
    context = {}
    categories = Category.objects\
                     .values('title')\
                     .annotate(category_population=Count('article'))\
                     .order_by('-category_population')[:3]
    context.update({'categories': categories})

    articles = Article.objects\
                   .values('title')\
                   .annotate(article_comments=Count('comment'))\
                   .order_by('-article_comments')[:10]
    context.update({'articles': articles})

    tags = Tag.objects\
                .values('title')\
                .annotate(tags_articles=Count('tag_article'))\
                .order_by('-tags_articles')[:10]
    context.update({'tags': tags})

    return render(request, 'blog/index.tpl', context)

def categories(request):
    context = {}
    categories = Category.objects \
                     .all() \
                     .annotate(category_articles=Count('article')) \
                     .order_by('-category_articles')
    context.update({'categories': categories})
    return render(request, 'blog/categories.tpl', context)

def category(request, **kwargs):
    context = {}
    category = Category.objects.get(id=kwargs.get('category_id'))
    context.update({'category': category})

    top_articles = Article.objects\
        .values('title', 'description')\
        .filter(article_category=kwargs.get('category_id'))\
        .annotate(articles_comments=Count('comment')) \
        .order_by('-articles_comments')
    context.update({'top_articles': top_articles})
    return render(request, 'blog/categories.tpl', context)

# Views:
# Each view:
# - nav bar(Home, Categories, Tags, Login / Logout)
# - breadcrumbs
# - footer(copyrights, cookie disclamer, user agreement)
#
# 3.
# CategoryView
# - category title(with 2 most commented articles and articles description)
# - list of articles(order by comments quantity)
# - pagination
#
# 4.
# ArticlesView
# - list of articles(order by comments quantity)
#
# 5.
# ArticleView
# - article title
# - article image
# - article content
#
# 6.
# TagView
# - list of tags(order by articles quantity) with 3 most commented articles
#
# 7.
# TagView
# - list of articles with category(order by comments quantity)
