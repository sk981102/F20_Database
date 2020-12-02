from django.shortcuts import render, redirect
from .forms import DataTypeForm
# Create your views here.

def createdatatype(request):
    if request.method == 'POST':
        form = DataTypeForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.save()
            return redirect('home')
    else:
        form = DataTypeForm()
    return render(request, 'createdatatype.html', {'form': form})
