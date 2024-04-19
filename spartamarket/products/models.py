from django.db import models
# from accounts.models import
from django.conf import settings


class HashtagInfo(models.Model):
    name = models.CharField(max_length=50)


class ProductInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users_by_product")
    hashtags = models.ManyToManyField(
        HashtagInfo, related_name="products_by_hashtag", symmetrical=False
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    hits = models.IntegerField(default=0)
    is_visible = models.BooleanField(default=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)


class CommentInfo(models.Model):
    product = models.ForeignKey(ProductInfo, on_delete=models.CASCADE, related_name="products_by_comment")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users_by_comment")
    comment = models.TextField()
    is_visible = models.BooleanField(default=True)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
