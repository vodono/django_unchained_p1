from django.urls import re_path
from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^categories/$',
            views.categories,
            name='categories'),
    re_path(r'^categories/(?P<category_title>[\w]+)/$',
            views.category,
            name='category'),
    # re_path(r'^categories/(?P<category_title>)/articles/$',
    #         views.ArticlesView.as_view(),
    #         name='articles'),
    # re_path(r'^categories/(?P<category_title>)/articles/?P<article_titles>/$',
    #         views.ArticleView.as_view(),
    #         name='article'),
    # re_path(r'^tags/$',
    #         views.TagsView.as_view(),
    #         name='tags'),
    # re_path(r'^tags/(?P<tag_title>)/$',
    #         views.TagView.as_view(),
    #         name='tag'),
]
