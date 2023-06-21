from django.urls import reverse
from django.contrib import sitemaps
from .models import Product

class StaticSiteMaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["home:home","home:products"]

    def location(self, item):
        return reverse(item)

class DynamicSiteMaps(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return Product.objects.filter(status=True).order_by("created_date")


    def location(self, obj):
        return '/product-informations/%s'%obj.id