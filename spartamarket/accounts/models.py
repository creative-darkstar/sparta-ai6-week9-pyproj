from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from products.models import ProductInfo


class UserInfo(AbstractUser):
    src = models.ImageField(
        upload_to="images/",
        blank=True,
    )
    carts = models.ManyToManyField(
        ProductInfo, related_name="cart_users", blank=True
    )
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )
