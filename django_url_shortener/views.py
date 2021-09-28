from django.views import View
from . import models
from django.http import HttpResponse, HttpResponseRedirect, Http404
import datetime

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = models.ShortUrl.objects.filter(shortcode__iexact=shortcode)
        if qs.count() != 1 and not qs.exists():
            raise Http404
        obj = qs.first()

        if self.check_expiry(obj):
            if obj.password and obj.user != request.user:
                #need to redirect to password form 
                return HttpResponse("URL is password protected")
            models.ClickEvent.objects.create_event(obj)
            return HttpResponseRedirect(obj.url)
        else:
            return HttpResponse("URL have been expired")


    def check_expiry(self, object):
        if not object.expiry_date:
            return True
        else:
            tz_info =object.expiry_date.tzinfo
            if object.expiry_date > datetime.datetime.now(tz_info):
                return True
            else:
                return False
