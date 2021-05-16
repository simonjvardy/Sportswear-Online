# Code adapted from CI Boutique Ado mini project

from django import forms
from .models import (
    Product, Gender, ArticleType, MasterCategory, SubCategory)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        gender = Gender.objects.all()
        article_type = ArticleType.objects.all()
        master_category = MasterCategory.objects.all()
        sub_category = SubCategory.objects.all()
        gender_display_name = [(
            g.id,
            g.gender_display_name()
        ) for g in gender]
        article_type_display_name = [(
            at.id,
            at.article_type_display_name()
        ) for at in article_type]
        master_category_display_name = [(
            mc.id,
            mc.master_category_display_name()
        ) for mc in master_category]
        sub_category_display_name = [(
            sc.id,
            sc.sub_category_display_name()
        ) for sc in sub_category]

        self.fields['gender'].choices = gender_display_name
        self.fields['article_type'].choices = article_type_display_name
        self.fields['master_category'].choices = master_category_display_name
        self.fields['sub_category'].choices = sub_category_display_name
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'
