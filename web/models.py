from django.db import models
from datetime import datetime,timedelta


class PublisherModel(models.Model):
	name = models.CharField(max_length=80)
	logourl = models.URLField(max_length=300)
	is_active = models.BooleanField(default=True)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name


class ArticleModel(models.Model):
	publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
	title = models.CharField(max_length=80)
	content = models.TextField()
	published_date = models.DateField()
	published = models.BooleanField(default=True)
	is_active = models.BooleanField(default=True)
	average_ratings = models.PositiveIntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.title