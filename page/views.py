from django.views.generic.base import View
from django.views.generic.edit import DeleteView
from page.forms import PageForm, WidgetPhotoForm, WidgetTextForm,WidgetOnlyTextForm
from page.models import Widget,WidgetGalery,WidgetGalleryPhotos, WidgetOnlyText, WidgetPhoto, WidgetText
from django.shortcuts import get_object_or_404, render,redirect
from faculties.models import Page, PageCategory
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.urls import reverse,reverse_lazy
import json

# Create your views here.

class WidgetTextUpdateView(View):

    def post(self,request,pk):

        widget = json.loads(request.body)
        type = widget['type']
 
        if type == "widgettext":
            widgetObject = get_object_or_404(WidgetText,id=pk)
            if widgetObject:
                widgetObject.title = widget['title']
                widgetObject.description = widget['description']
                widgetObject.save()
        
        if type == "widgetonlytext":
            widgetObject = get_object_or_404(WidgetOnlyText,id=pk)
            if widgetObject:
                widgetObject.description = widget['description']
                widgetObject.save()

        if type == "widgetphoto":
            widgetObject = get_object_or_404(WidgetPhoto,id=pk)
            if widgetObject:
                widgetObject.title = widget['title']
                widgetObject.description = widget['description']
                widgetObject.save()

        return HttpResponse("Hello")
class PageListView(ListView):
    model = Page
    context_object_name = 'pages'
    template_name = 'page/page_list.html'

    def get_queryset(self):
        return Page.objects.filter(category_id=self.kwargs['pk']).order_by('order')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PageCategory.objects.all()
        return context

class PageDetailView(DetailView):
    model = Page
    context_object_name = 'page'
    template_name = 'page/pageDetail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context['page']
        pageWidgets = Widget.objects.filter(page=page).order_by('order')
        context['pageWidgets'] = pageWidgets
        return context

class PageCreateView(CreateView):

    model = Page
    template_name = 'page/page_form.html'
    form_class = PageForm

class PageUpdateView(UpdateView):

    model = Page
    template_name = 'page/page_form.html'
    form_class = PageForm


class PageDeleteView(DeleteView):

    model = Page
    template_name = "page/page_confirm_delete.html"

    def get_success_url(self):    
        return reverse_lazy('pageListView', kwargs = {'pk': self.kwargs['cat_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_id'] = self.kwargs['cat_id']
        return context
    

class PageCategoryCreateView(CreateView):

    model = PageCategory
    fields = ['name','name_kk','name_en','linkto']
    template_name = 'page/pageCategory_form.html'

def orderedPages(request):

    if request.method == "POST":
        pages = json.loads(request.body)
    
        for b in pages:
            page = get_object_or_404(Page, id=int(b['pk']))
            page.order = b['order']
            page.save()
        return HttpResponse('saved')


def orderedWidgets(request):

    if request.method == "POST":
        widgets = json.loads(request.body)
    
        for b in widgets:
            page = get_object_or_404(Widget, id=int(b['pk']))
            page.order = b['order']
            page.save()
        return HttpResponse('saved')


def addWidget(request,*args,**kwargs):

    page = kwargs['pk']
    typeWidget = request.POST.get('type')

    
    if typeWidget == "widgettext":

        widgetTextForm = WidgetTextForm(request.POST or None)
        if widgetTextForm.is_valid():
            widgetText = widgetTextForm.save()

        widget = Widget.objects.create(
            content_object=widgetText,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetonlytext":

        widgetOnlyTextForm = WidgetOnlyTextForm(request.POST or None)

        if widgetOnlyTextForm.is_valid():
            widgetText = widgetOnlyTextForm.save()

        widget = Widget.objects.create(
            content_object=widgetText,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetphoto":
        
        widgetPhotoForm = WidgetPhotoForm(request.POST or None,request.FILES or None)
        if widgetPhotoForm.is_valid():
            widgetPhoto = widgetPhotoForm.save()
        
        widget = Widget.objects.create(
            content_object=widgetPhoto,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    elif typeWidget == "widgetgallery":
        
        widgetGallery = WidgetGalery.objects.create(
            title = request.POST.get('title')
        )
        widgetGallery.save()


        for image in request.FILES.getlist('images'):
            
            widgetGalleryPhoto = WidgetGalleryPhotos.objects.create(
                image=image,
                widgetGalery=widgetGallery
            )
            widgetGalleryPhoto.save()

        widget = Widget.objects.create(
            content_object=widgetGallery,
            page_id=page,
            widgettype=typeWidget
        )
        widget.save()

    
    return redirect(str(reverse('pageDetailView',  kwargs = {'pk' : page, })))