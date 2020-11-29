from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import *
from .forms import TaskCreateForm
from task.models  import Task #,TaskDataTable

# Create your views here.
def create(request):
    if request.method=='POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            thisadmin=MyAdmin.objects.get(user_id=request.user.user_id)
            '''tskdtobj=TaskDataTable(Name=request.POST.get('TaskDataTableName',''), Scheme=request.POST.get('TaskDataTableScheme',''))
            tskdtobj.save'''

            tskobj=Task(task_name=request.POST.get('Name',''), admin=thisadmin, description=request.POST.get('Comment',''), mincycle=request.POST.get('mincycle','')) #taskdatatable needed
            tskobj.save()
            return render(request, 'TaskCreateSuccess.html')
        #return redirect('/pjadmin')
        return render(request, 'TaskCreateFail.html')
    else:
        form = TaskCreateForm()
 
    return render(request, 'TaskCreate.html', {'form': form})

def manage(request):
    tasks=Task.objects.all()
    return render(request, 'TaskManage2.html', {"tasks": tasks})

def task_submitters(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'TaskSubmitters.html',context={'task':task})
