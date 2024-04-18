from django.db import models
# from accounts.models import
from django.contrib.auth.models import User


class ProductInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_by_product")
    # hashtags = models.CommaSeparatedIntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()
    hits = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)


class HashtagInfo(models.Model):
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, related_name="products_by_hashtag")
    name = models.CharField(max_length=50)


class CommentInfo(models.Model):
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, related_name="products_by_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_by_comment")
    comment = models.TextField()
    is_visible = models.BooleanField(default=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
