from django.conf import settings
from django.db import models
try:
    from django.utils.encoding import smart_text
except:
    from django.utils.encoding import smart_str as smart_text
from django.urls import reverse
from .validators import validate_url
from django.contrib.auth import get_user_model
import werkzeug.security
import random
import string

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 4)
SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)
BASE_URL = getattr(settings, "BASE_URL", "http://127.0.0.1:8000")

User = get_user_model()

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits + string.ascii_uppercase):
        return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(size=SHORTCODE_MIN):
    new_code = code_generator(size=size)
    qs_exists = ShortUrl.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code

class ShortURLManager(models.Manager):
    
    def all(self, *args, **kwargs):
        qs_main = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = ShortUrl.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode()
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class ShortUrl(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank= True, related_name='short_urls')
    url = models.CharField(max_length=256, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    expiry_date = models.DateTimeField(blank=True, null= True, default = None)
    password = models.CharField(max_length=255, blank=True, null= True, default = None)
    active = models.BooleanField(default=True)
    objects = ShortURLManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode()
        if self.pk is None and self.password:
            self.password = werkzeug.security.generate_password_hash(self.password)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(ShortUrl, self).save(*args, **kwargs)

    def __str__(self):
        return smart_text(self.url)

    def __unicode__(self):
        return smart_text(self.url)

    def get_short_url(self):
        url_path = BASE_URL+reverse("scode", kwargs={'shortcode': self.shortcode})
        return url_path



class ClickEventManager(models.Manager):
    def create_event(self, shInstance):
        if isinstance(shInstance, ShortUrl):
            obj, created = self.get_or_create(sh_url=shInstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    sh_url    = models.OneToOneField(ShortUrl,on_delete=models.CASCADE,related_name='clicks')
    count       = models.IntegerField(default=0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
