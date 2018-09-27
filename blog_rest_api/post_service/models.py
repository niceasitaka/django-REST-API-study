from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=1024)
	body = models.CharField(max_length=4096)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	regdate = models.DateTimeField(auto_created=True, auto_now_add=True)
	# 시간이 자동으로 생성되고 / 현재 시간이 자동으로 기록되는