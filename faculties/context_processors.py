from faculties.models import PageCategory


def page_categories(request):

    pageCats = PageCategory.objects.all()
    internatiolization = PageCategory.objects.get(id=3)

    return {
        'pageCats':pageCats,
        'internatiolization':internatiolization
    }