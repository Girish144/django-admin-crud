from django.contrib import admin
from .models import product_model

# Register your models here.
class product(admin.ModelAdmin):
    list_display=['name','price','qty','loc']
    list_editable=['qty']
    list_per_page=2
    list_filter=['name']
    list_display_links=['name']


admin.site.register(product_model,product)