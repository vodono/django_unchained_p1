{% extends "core/base.tpl" %}

{% block title %}Categories{% endblock %}


{% load django_bootstrap_breadcrumbs %}

{% block breadcrumbs %}
    {{ block.super }}
    {% breadcrumb "Categories" "/" %}
{% endblock %}


{% block content %}
    <h1>Django Unchained Blog</h1>
    <br>

    <h2>Categories</h2>
    {% for category in categories %}
        <h2><a href="{{ category.title.lower }}/">{{ category.title }}</a></h2>
        <img src="{{ category.image.url }}"/>
        <hr>
    {% endfor %}
    <br>
{% endblock %}
