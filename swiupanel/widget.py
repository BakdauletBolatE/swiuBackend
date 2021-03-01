from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .forms import PageForm,WidgetItemsForm
from faculties.models import Page
from .models import Widget,WidgetItems, WidgetType
import json
def indexPage(request):

    pages = Page.objects.all()
    context = {
            'pages': pages
    }
    return render(request, 'swiupanel/Page/listView.html',context)

def viewPage(request,id):
    iform = WidgetItemsForm()
    page = Page.objects.get(id=id)
    context = {
            'page': page,
            'iform':iform
    }
    return render(request, 'swiupanel/Page/view.html',context)



def addPage(request):
    if request.method == "POST":
        form = PageForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('pageIndex')
        else:
            return HttpResponse("ЧТо за ошибка угадайка")
    else:   
        form = PageForm()
        context = {
            'form': form
        }
        return render(request, 'swiupanel/Page/add.html',context)


def addWidgetType(request):
    if request.method == "POST":
        data = json.loads(request.body);
        id = data['pageId']
        widgetType = data['widgetType']
        widget = Widget.objects.create(page_id=id,widget_type_id=widgetType)
        widget.save()
        return JsonResponse(request.POST)

def getWidgetJson(request):

    widget = list(Widget.objects.values())

    return JsonResponse({'widget':widget})


def addWidgetItem(request):

    if request.method == "POST":

        form = WidgetItemsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            print("saved")
            return HttpResponse('Its saved')
        else:
            print('error')
            return HttpResponse("Error")