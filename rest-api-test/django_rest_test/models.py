from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=256)
	content = models.CharField(max_length=2948)
	reg_date = models.DateTimeField(auto_created=True, auto_now=True)
	# 시간이 자동으로 생성되고 / 현재 시간이 자동으로 기록되는
	
