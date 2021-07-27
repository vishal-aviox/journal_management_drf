
from web import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('publisher', views.PublisherView.as_view()),
    path('article', views.ArticleView.as_view()),
    path('deactive_articles', views.DeactiveArticles.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
