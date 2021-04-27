from django.contrib import admin
from .models import (
    Product, Gender, ArticleType, MasterCategory, SubCategory
)

# Register your models here.
admin.site.register(Product)
admin.site.register(Gender)
admin.site.register(ArticleType)
admin.site.register(MasterCategory)
admin.site.register(SubCategory)
