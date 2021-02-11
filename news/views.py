from django.shortcuts import render,redirect
from .forms import QuestionsForm,PostCommentsForm
from .models import *
from django.http import JsonResponse
from news.decoretors import counted
from faculties.models import PageCategory
import json




# Create your views here.
@counted
def postDetailView(request,url):
    post = Post.objects.get(slug=url)
    page = PageHit.objects.get(url=request.path)
    pageCats = PageCategory.objects.all()
    context = {
        'page':page,
        "post":post,
        'pageCats':pageCats
    }
    return render(request,"news/newsDetail.html",context)


def QuestionsView(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('jib,rf')
    else:
        form = QuestionsForm()

    return render(request,'main/pages/review.html',{'form':form})

def addPostComment(request):
    if request.method == "POST":
        data = json.loads(request.body)    
        url = data["slug"]
        desciption = data["desciption"]
        post = Post.objects.get(slug=url)
        comment = PostComments(description=desciption,post=post,author="ss")
        comment.save()

    comment = PostComments.objects.values('description', 'id').all()


    
    return JsonResponse({'comments': list(comment)})
    
def likesCount(request,url):
    post = Post.objects.get(slug=url)
    likes = post.likes.count()
    return JsonResponse({'like': likes})

def likePost(request):
    if request.method == "POST":
        print(request.body)
        data = json.loads(request.body)
        url = data["slug"]
        session_key = data["session_key"]
        post = Post.objects.get(slug=url)
        like,created = Like.objects.get_or_create(
            post=post,
            user=session_key
        )
        print(session_key)
        if created == False:
            print(session_key)
            like.delete()
        

    return redirect('index')
    

def viewPostComment(request,url):
    post = Post.objects.get(slug=url)
    comment = PostComments.objects.values('description', 'id','author').filter(post=post)[:5]
    return JsonResponse({'comments': list(comment)})