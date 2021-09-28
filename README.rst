=====
Django URL Shortener
=====

Django URL Shortener is a Django app to to include URL Shortening feature in your Django Project

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_url_shortener" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_url_shortener',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('s/', include('django_url_shortener.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. [Optional] Upate configs in settings.py
    SHORTCODE_MIN = 4
    SHORTCODE_MAX = 20
    BASE_URL = "https://mysite.com"

5. Import shorten_url method 
    from django_url_shortener.utils import shorten_url

6. Shorten your URL

    created, short_url = shorten_url("https://github.com/rishav00a/django_url_shortener")
    created, short_url = shorten_url("https://github.com/rishav00a/django_url_shortener/issues","xyzw")