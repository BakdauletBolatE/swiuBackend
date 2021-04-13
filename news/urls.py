from django.urls import path
from .views import *

urlpatterns = [
    path('questions/',QuestionsView,name="questionsView"),
    path('comments/add',addPostComment,name="commentsAdd"),
    path('comments/<slug:url>/',viewPostComment,name="commentsView"),
    path('post/like',likePost,name="postLike"),
    path('post/likecount/<slug:url>',likesCount),
    path('post/<slug:url>',postDetailView,name="postDetailView"),
    path('allposts/<int:pk>',postListView,name="postListView"),
    path('requestadd/',requestAdd,name="requestadd")
]