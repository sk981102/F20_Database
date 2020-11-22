from django.shortcuts import render, redirect
from .models import *
from .forms import TaskCreateForm
# Create your views here.
def create(request):
    if request.method=='POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/pjadmin')
    else:
        form = TaskCreateForm()
 
    return render(request, 'TaskCreate.html', {'form': form})
