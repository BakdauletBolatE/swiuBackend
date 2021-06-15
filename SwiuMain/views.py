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
    posts = Post.objects.filter(category_id=1).order_by('-created_at').all()[:3]
    ads = Post.objects.filter(category_id=2).order_by('-created_at').all()[:3]
    slides = Slides.objects.all().order_by('-id')
    context = {
        'quotes':quotes,
        'posts':posts,
        'ads':ads,
        'slides':slides,
    }
    return render(request,'main/index.html',context)

def aboutUs(request):
    intarnationalStaff = Staff.objects.filter(staffCat_id=1)
    context = {'intarnationalStaff':intarnationalStaff}
    return render(request,'main/pages/about-us.html', context)

def facultView(request):
    facults = Facult.objects.all()
    context = {'facults':facults}
    return render(request,'facult/index.html',context)

def pageView(request,url):
    page = Page.objects.get(slug=url)
    context = {'page':page}
    return render(request,'facult/page.html',context)

def opView(request):
    facult = Facult.objects.all()
    context = {'facult': facult}
    return render(request, 'main/pages/op.html', context)

def accreditation(request):
    return render(request, 'main/pages/accreditation.html')

def enrolleView(request):
    return render(request, 'pages/enrolle.html')

def toTheStudentsView(request):
    return render(request, 'pages/toTheStudents.html')
