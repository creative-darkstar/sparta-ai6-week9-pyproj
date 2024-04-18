from django.db import models


# class UserInfo(models.Model):
#     name = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     userid = models.CharField(max_length=50)
#     password = models.CharField()
#     email = models.CharField(max_length=50)
#     src = models.CharField()
#     create_dt = models.DateTimeField(auto_now_add=True)
#     level = models.IntegerField(max_length=10)


# class CartInfo(models.Model):
#     user_idx = models.ForeignKey()
#     content_idx = models.ForeignKey()
#     create_dt = models.DateTimeField(auto_now_add=True)
#
#
# class FollowInfo(models.Model):
#     user_idx = models.ForeignKey()
#     f_user_idx = models.ForeignKey()
#     create_dt = models.DateTimeField(auto_now_add=True)
