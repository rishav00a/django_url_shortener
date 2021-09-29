
=====================
Django URL Shortener
=====================

Django URL Shortener is a Django app to to include URL Shortening feature in your Django Project

Install this package to your Django project::

    pip install django-url-shortener-app


Links
-------

`Github <https://github.com/rishav00a/django_url_shortener>`_

`PyPI <https://pypi.org/project/django-url-shortener-app/>`_


Quick start
-----------

1. Add ``django_url_shortener`` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_url_shortener',
    ]

2. Include the django_url_shortener URLconf in your project urls.py like this::

    path('s/', include('django_url_shortener.urls')),

3. Run ``python manage.py migrate`` to create the models.

4. [Optional] Upate configs in settings.py::

    SHORTCODE_MIN = 4
    SHORTCODE_MAX = 20
    BASE_URL = "https://mysite.com"

5. Import shorten_url method ::

    from django_url_shortener.utils import shorten_url

6. Shorten your URL::

    created, message = shorten_url(long_url, short_code)
    '''
    long_url: String : Required
    short_code: String : Optional
    created: Boolean : True if url shortened successfully
    message: String : created short url will be returned if url shortened successfully, othewrwise error message will be returned
    '''
    
7. Example Usage::

    created, short_url = shorten_url("https://github.com/rishav00a/django_url_shortener")
    created, short_url = shorten_url("https://github.com/rishav00a/django_url_shortener/issues","xyzw")
    
