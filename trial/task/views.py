from django.shortcuts import render
from django.views import generic
from task.models import Task
from django.shortcuts import get_object_or_404

def TaskDetailView(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', context={'task': task})

def ListFunc(request):
    data = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': data})
