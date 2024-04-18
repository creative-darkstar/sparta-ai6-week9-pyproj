from django.db import models
from django.contrib.auth.models import User


# class UserInfo(models.Model):
#     name = models.CharField(max_length=50)
#     nickname = models.CharField(max_length=50)
#     userid = models.CharField(max_length=50)
#     password = models.CharField()
#     email = models.CharField(max_length=50)
#     src = models.CharField()
#     create_dt = models.DateTimeField(auto_now_add=True)
#     level = models.IntegerField(max_length=10)


# class FollowInfo(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     f_user = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_dt = models.DateTimeField(auto_now_add=True)
