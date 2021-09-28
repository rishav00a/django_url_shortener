from django.contrib import admin
from .models import ShortUrl


class ShortURLAdmin(admin.ModelAdmin):
    """
    ModelAdmin for ShURLAdmin.
    """
    ordering = ('-updated_at', )
    list_filter = (
        'updated_at',
        'user'
    )
    search_fields = (
        'shortcode',
        'url',
        'user',
    )
    list_display = (
        'user',
        'url',
        'shortcode',
        'updated_at',
    )

admin.site.register(ShortUrl,ShortURLAdmin)
