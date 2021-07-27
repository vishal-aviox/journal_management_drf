from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PublisherModel, ArticleModel


class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = PublisherModel
		fields = "__all__"
			
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleModel
		fields = "__all__"

	def to_representation(self, instance):
		self.fields['publisher'] =  PublisherSerializer()
		return super(ArticleSerializer, self).to_representation(instance)