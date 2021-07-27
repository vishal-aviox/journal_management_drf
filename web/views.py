from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PublisherModel, ArticleModel
from .serializers import PublisherSerializer, ArticleSerializer


class PublisherView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		context: dict = {}
		active_publishers = PublisherModel.objects.filter(is_active=True)
		serializer = PublisherSerializer(active_publishers, many=True)
		context['status'] = True
		context['data'] = serializer.data
		return Response(context)

class ArticleView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		context = {}
		articles = ArticleModel.objects.filter(is_active=True,published_date__gt='2020-06-30')
		serializer = ArticleSerializer(articles,many=True)
		context['status'] = True
		context['data'] = serializer.data
		return Response(context)

	def post(self, request, format=None):
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeactiveArticles(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, format=None):
		context = {}
		ArticleModel.objects.filter(is_active=True,average_ratings__lt=3,published_date__lt="2020-10-05").update(is_active=False)

		context['status'] = True
		context['maeeage'] = 'Articles successfully deactivated.'
		return Response(context)