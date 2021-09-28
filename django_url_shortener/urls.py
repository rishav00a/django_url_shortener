
from django.conf.urls import url
from .views import URLRedirectView


urlpatterns = [
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),
]
