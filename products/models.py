from django.db import models


class Gender(models.Model):
    """
    Model Gender allows the grouping of product
    for easier searches
    """
    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def gender_display_name(self):
        return self.display_name


class ArticleType(models.Model):
    """
    Model ArticleType allows the grouping of products
    for easier searches by type of item or product
    """
    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def article_type_display_name(self):
        return self.display_name


class MasterCategory(models.Model):
    """
    Model MasterCategory allows the grouping of products
    for easier searches by main category of item or product
    """
    class Meta:
        verbose_name_plural = 'Master Categories'

    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def master_category_display_name(self):
        return self.display_name


class SubCategory(models.Model):
    """
    Model SubCategory allows the grouping of products
    for easier searches by sub-category of item or product
    """

    class Meta:
        verbose_name_plural = 'Sub Categories'

    name = models.CharField(
        max_length=254)
    display_name = models.CharField(
        max_length=254)

    def __str__(self):
        return self.name

    def sub_category_display_name(self):
        return self.display_name


class Product(models.Model):
    """
    Model Product contains the detailed product information
    with foreign keys to the related category models
    """

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=6,
        decimal_places=2)
    sku = models.CharField(
        max_length=254)
    name = models.CharField(
        max_length=254)
    product_description = models.TextField()
    sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True)
    gender = models.ForeignKey(
        'Gender',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    master_category = models.ForeignKey(
        'MasterCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sub_category = models.ForeignKey(
        'SubCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    article_type = models.ForeignKey(
        'ArticleType',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    image = models.ImageField(
        blank=True,
        null=True)

    def __str__(self):
        return self.name
