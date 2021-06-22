from django.shortcuts import render,redirect
from .forms import QuestionsForm,RequestForm
from .models import *
from django.http import JsonResponse
from news.decoretors import counted
from faculties.models import PageCategory
from django.core.paginator import Paginator
import json
from django.contrib import messages




# Create your views here.
@counted
def postDetailView(request,url):
    post = Post.objects.get(slug=url)
    page = PageHit.objects.get(url=request.path)
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'page':page,
        "post":post,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,"news/newsDetail.html",context)


def QuestionsView(request):
    pageCats = PageCategory.objects.all()
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('jib,rf')
    else:
        form = QuestionsForm()
    
    context = {
        'form':form,
        'pageCats': pageCats,
    }

    return render(request,'main/pages/review.html',context)

def likePost(request):
    if request.method == "POST":
        data = json.loads(request.body)
        url = data["slug"]
        session_key = data["session_key"]
        post = Post.objects.get(slug=url)
        like,created = Like.objects.get_or_create(
            post=post,
            user=session_key
        )
        print(like)
        print(created)
        if created == False:
            like.delete()


    return redirect('index')
    

def postListView(request,pk):
    category = PostCategories.objects.get(id=pk)
    post = Post.objects.filter(category_id=pk).order_by('-created_at')
    paginator = Paginator(post, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category':category,
        'page_obj': page_obj,
    }

    return render(request,'news/newsList.html',context)
    

def requestAdd(request):

    if request.method == 'POST':

        form = RequestForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Уважаемый {form.cleaned_data['name']} вы подписались на нашу обновление")
            return redirect('index')
        else:
            messages.success(request, f"Ошибочка вышла")
            return redirect('index')