from page.models import Widget
from faculties.models import Page
from django.shortcuts import render
from faculties.models import Facult,PageCategory
from staff.models import Staff
from news.models import Quote,PageHit,PostComments,Post, Slides

from news.decoretors import counted


@counted
def index(request):
    if not request.session or not request.session.session_key:
        request.session.save()


    quotes = Quote.objects.all()[:3]
    pageCats = PageCategory.objects.all()
    posts = Post.objects.filter(category_id=1).order_by('-created_at').all()[:3]
    ads = Post.objects.filter(category_id=2).order_by('-created_at').all()[:3]
    internatiolization = PageCategory.objects.get(id=3)
    slides = Slides.objects.all()
    context = {
        'quotes':quotes,
        'posts':posts,
        'pageCats':pageCats,
        'ads':ads,
        'slides':slides,
        'internatiolization':internatiolization
    }
    return render(request,'main/index.html',context)

def aboutUs(request):
    intarnationalStaff = Staff.objects.filter(staffCat_id=1)
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'intarnationalStaff':intarnationalStaff,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,'main/pages/about-us.html', context)

def facultView(request):

    facults = Facult.objects.all()
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)
    context = {
        'facults':facults,
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }
    return render(request,'facult/index.html',context)

def pageView(request,url):
    pageCats = PageCategory.objects.all()
    page = Page.objects.get(slug=url)
    internatiolization = PageCategory.objects.get(id=3)
    widgets = Widget.objects.filter(page=page).order_by('order')
    context = {
        'page':page,
        'pageCats':pageCats,
        'widgets':widgets,
        'internatiolization':internatiolization
    }
    return render(request,'facult/page.html',context)

def opView(request):

    facult = Facult.objects.all()
    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'facult': facult,
        'pageCats': pageCats,
        'internatiolization':internatiolization
    }
    return render(request, 'main/pages/op.html', context)

def accreditation(request):

    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'pageCats': pageCats,
        'internatiolization':internatiolization
    }
    return render(request, 'main/pages/accreditation.html', context)

def enrolleView(request):

    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'pageCats': pageCats,
        'internatiolization':internatiolization
    }
    return render(request, 'pages/enrolle.html', context)

def toTheStudentsView(request):

    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    context = {
        'pageCats': pageCats,
        'internatiolization':internatiolization
    }
    return render(request, 'pages/toTheStudents.html', context)
