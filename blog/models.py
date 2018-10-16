from django.db import models
from django.utils import timezone


class Post(models.Model):
	"""データベースフィールド
	
	author --- 記事の筆者
	title --- 記事のタイトル
	text --- 記事本文
	created_date --- 記事作成日
	published_date
	"""
	
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)
	
	
	def publish(self):
		self._published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title