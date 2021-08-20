from django.shortcuts import render, redirect
from .forms import ZayavkaApp
from django.contrib import messages

def main(request):

    if request.method == "POST":

        form = ZayavkaApp(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Файлы были успешно загружены')
            return redirect('/')
        else:
            print('eror')
            print(form.errors)
            messages.error(request, 'Форма неверно заполнена ')
            return redirect('/')    

    context = {
        'form': ZayavkaApp()
    }
    return render(request, 'change.html', context)
