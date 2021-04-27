from django.urls import path
from .views import *

urlpatterns = [
    path('questions/',QuestionsView,name="questionsView"),
    path('posts/like',likePost,name="postLike"),
    path('post/<slug:url>',postDetailView,name="postDetailView"),
    path('allposts/<int:pk>',postListView,name="postListView"),
    path('requestadd/',requestAdd,name="requestadd")
]