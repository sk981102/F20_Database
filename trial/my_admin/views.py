from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import path 
from .models import *
from .forms import TaskCreateForm, PassStandardForm
from task.models  import Task,ApplyTask #,TaskDataTable
from submitter.models import Submitter
from accounts.models import UserProfile
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

def task_pass_standard(request, task_id):
    thistask=get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = PassStandardForm(request.POST)
        if form.is_valid():
                thistask.pass_standard = request.POST['pass_standard']
                thistask.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect('home')
        else:
                messages.error(request, 'Please correct the error below.')
    else:
        form = PassStandardForm()        
    return render(request, 'PassStandard.html', {'form': form})
 
def task_submitters(request, pk):
    thistask = get_object_or_404(Task, pk=pk)
    approved_submitters=ApplyTask.objects.filter(task=thistask, approved=1)
    pending_submitters=ApplyTask.objects.filter(task=thistask, approved=0)
    return render(request, 'TaskSubmitters.html',context={'task':thistask, 'approved_submitter':approved_submitters,'pending_submitter':pending_submitters})

def sub_approve(request,task_id,user_id): 
    thistask=get_object_or_404(Task, pk=task_id)
    thispropile=get_object_or_404(UserProfile, username=user_id)
    thissubmitter=get_object_or_404(Submitter, pk=thispropile.user_id)
    thisobj=get_object_or_404(ApplyTask, task=thistask, submitter=thissubmitter)
    thisobj.approved=1
    thisobj.save()
    return render(request, 'Approve.html', context={'obj':thisobj})
