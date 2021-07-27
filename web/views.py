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
		""" this api returns active publishers """
		try:
			context: dict = {}
			active_publishers = PublisherModel.objects.filter(is_active=True)
			serializer = PublisherSerializer(active_publishers, many=True)
			context['status'] = True
			context['data'] = serializer.data
			context['message'] = str('Active Publishers')

		except Exception as e:
			context['status'] = False
			context['data'] = []
			context['error'] = str(e)
		
		return Response(context, status=status.HTTP_200_OK)

class ArticleView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		""" this api returns active articles and published date is greater than 2020-06-30 """
		try:
			context: dict = {}
			articles = ArticleModel.objects.filter(is_active=True,published_date__gt='2020-06-30')
			serializer = ArticleSerializer(articles,many=True)
			context['status'] = True
			context['data'] = serializer.data
			context['message'] = str('Active Articles')

		except Exception as e:
			context['status'] = False
			context['data'] = []
			context['error'] = str(e)

		return Response(context, status=status.HTTP_200_OK)

	def post(self, request, format=None):
		try:
			serializer = ArticleSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)

		except Exception as e:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeactiveArticles(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, format=None):

		""" this api deactivates all articles having published date is less than 2020-10-05 and average_ratings less than 3 """
		try:
			context: dict = {}
			ArticleModel.objects.filter(is_active=True,average_ratings__lt=3,published_date__lt="2020-10-05").update(is_active=False)
			context['status'] = True
			context['message'] = 'Articles successfully deactivated.'

		except Exception as e:
			context['status'] = False
			context['data'] = []
			context['error'] = str(e)
		return Response(context, status=status.HTTP_200_OK)