from faculties.models import Page
from django.shortcuts import render
from faculties.models import Facult,PageCategory
from staff.models import Staff
from news.models import Quote,PageHit,PostComments,Post

from news.decoretors import counted


@counted
def index(request):
    if not request.session or not request.session.session_key:
        request.session.save()


    quotes = Quote.objects.all()[:3]
    pageCats = PageCategory.objects.all()
    posts = Post.objects.filter(category_id=1).order_by('-created_at').all()[:3]
    ads = Post.objects.filter(category_id=2).order_by('-created_at').all()[:3]
    context = {
        'quotes':quotes,
        'posts':posts,
        'pageCats':pageCats,
        'ads':ads
    }
    return render(request,'main/index.html',context)

def aboutUs(request):
    intarnationalStaff = Staff.objects.filter(staffCat_id=1)
    pageCats = PageCategory.objects.all()

    context = {
        'intarnationalStaff':intarnationalStaff,
        'pageCats':pageCats
    }
    return render(request,'main/pages/about-us.html', context)

def facultView(request):

    facults = Facult.objects.all()
    pageCats = PageCategory.objects.all()
    context = {
        'facults':facults,
        'pageCats':pageCats
    }
    return render(request,'facult/index.html',context)

def pageView(request,url):
    pageCats = PageCategory.objects.all()
    page = Page.objects.get(slug=url)
    context = {
        'page':page,
        'pageCats':pageCats
    }
    return render(request,'facult/page.html',context)
