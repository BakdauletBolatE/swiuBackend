from django.shortcuts import render,redirect
from .forms import QuestionsForm
# Create your views here.

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
