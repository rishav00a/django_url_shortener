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

4. ...

5. ...