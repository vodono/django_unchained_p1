{% extends "core/base.tpl" %}

{% block title %}Category{% endblock %}


{% load django_bootstrap_breadcrumbs %}

{% block breadcrumbs %}
    {{ block.super }}
    {% breadcrumb "Categories" "/" %}
    {% breadcrumb "category.category" "/" %}
{% endblock %}


{% block content %}
    <h1>Django Unchained Blog</h1>
    <br>

    <h2>{{category.title}}</h2>
    {% for article in top_articles %}
        <h2><a href="categories/{{ article.title.lower }}/">{{ article.title }}</a></h2>
        <img src="{{ article.image.url }}"/>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
