from . import models

def shorten_url(long_url, shortcode=None):
    if shortcode:
        if not models.ShortUrl.objects.filter(shortcode=shortcode).exists():
            obj = models.ShortUrl.objects.create(
                url = long_url,
                shortcode = shortcode
            )
        else:
            return False, "Shortcode not available"
    else:
        try:
            obj, _ = models.ShortUrl.objects.get_or_create(url= long_url)
        except Exception as e:
            return False, str(e), 
    return True, obj.get_short_url()


