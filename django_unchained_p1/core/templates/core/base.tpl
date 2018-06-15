<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap.min.css">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>{% block title %}{% endblock %}</title>
    </head>
    <body>
        <style>
            body {background: pink}
        </style>

        <nav class="navbar navbar-dark bg-primary">
          <span class="navbar-text">
              <a href="/">Home</a>
              <a href="/categories">Categories</a>
              <a href="/tags">Tags</a>
              <a href="/login">Login/Logout</a>
          </span>
        </nav>

        {% load django_bootstrap_breadcrumbs %}

        {% block breadcrumbs %}
            {% clear_breadcrumbs %}
            {% breadcrumb "Home" "/" %}
        {% endblock %}

        {% block content_breadcrumbs %}
            {% render_breadcrumbs %}
        {% endblock %}

        <br>
        <div class="container-fluid">
            {% block content %}
            {% endblock %}
        </div>
        <footer>
            <style>
                footer {background: grey}
            </style>
            <div class="footer-bg">
            <div class="copyright">
                <p><strong>Django unchained experimental blog.</strong></p>
                <p>&copy; Santa</p>
            </div>
            </div>
        </footer>
    </body>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js"></script>
</html>
