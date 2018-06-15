{% extends 'core/base.tpl' %}

{% block title %}Login{% endblock %}

{% load django_bootstrap_breadcrumbs %}

{% block breadcrumbs %}
    {{ block.super }}
    {% breadcrumb "Login" "/" %}
{% endblock %}

{% block content %}
    <h2>Login</h2>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
    <button type="submit">Login</button>
    </form>
{% endblock %}
