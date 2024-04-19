from django import forms
from .models import ProductInfo, HashtagInfo, CommentInfo


class ProductInfoModelForm(forms.ModelForm):
    class Meta:
        model = ProductInfo
        fields = "__all__"
        exclude = (
            "user",
            "hashtags",
            "hits",
            "is_visible",
            "create_dt",
            "update_dt",
        )
