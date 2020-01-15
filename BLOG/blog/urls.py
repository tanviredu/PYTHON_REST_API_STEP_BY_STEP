from django.urls import path 
from .views import Articleview
from .views import SingleArticlePost
urlpatterns = [
  path('articles/',Articleview.as_view()),
  path('articles/<int:pk>',Articleview.as_view()),
  path('article/<int:pk>',SingleArticlePost.as_view())
]