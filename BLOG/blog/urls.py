from django.urls import path 
from .views import Articleview

urlpatterns = [
  path('articles',Articleview.as_view()),
  path('articles/<int:pk>',Articleview.as_view())
]