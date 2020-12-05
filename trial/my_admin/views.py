import pandas as pd
from pandas import DataFrame
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.db import connection
from django.urls import path 
from .models import *
from .forms import TaskCreateForm, PassStandardForm
from task.models  import Task,ApplyTask,TaskSchema
from submitter.models import Submitter
from accounts.models import UserProfile
from raw_data.models import RawDataType, RawDataSeqFile
from task.models  import Task,ApplyTask,TaskSchema
from submitter.models import Submitter
from accounts.models import UserProfile
from raw_data.models import RawDataType, RawDataSeqFile

# Create your views here.

def create(request):
    if request.method=='POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            thisadmin=MyAdmin.objects.get(user_id=request.user.user_id)


            schema_name = request.POST.get('TaskDataTableName', '')
            schema=request.POST.get('TaskDataTableScheme','')

            cursor = connection.cursor()
            cursor.execute(schema)
            cursor.close()


            tskobj=Task(task_name=request.POST.get('Name',''), admin=thisadmin,
                        description=request.POST.get('Comment',''), mincycle=request.POST.get('mincycle','')) #taskdatatable needed
            tskobj.save()

            task_schema=TaskSchema(task_id=tskobj,TaskDataTableName=schema_name,TaskDataTableScheme=schema)
            task_schema.save()

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
    thisrawtype = RawDataType.objects.filter(task=thistask.task_id).values_list('type_id',flat=True)
    rawnum = RawDataSeqFile.objects.filter(raw_data_type__in=thisrawtype)
    num = rawnum.count()
    approved_submitters=ApplyTask.objects.filter(task=thistask, approved=1)
    pending_submitters=ApplyTask.objects.filter(task=thistask, approved=0)

    #show data so far
    task_schema=TaskSchema.objects.filter(task_id=thistask).first()
    table = "SELECT * FROM " + task_schema.TaskDataTableName
    cursor = connection.cursor()
    cursor.execute(table)
    result = cursor.fetchall()


    return render(request, 'TaskSubmitters.html',context={
        'task':thistask, 'approved_submitter':approved_submitters,'pending_submitter':pending_submitters,
        'num':num, 'rawnum': rawnum, 'task_table':result})

def sub_approve(request,task_id,user_id): 
    thistask=get_object_or_404(Task, pk=task_id)
    thispropile=get_object_or_404(UserProfile, username=user_id)
    thissubmitter=get_object_or_404(Submitter, pk=thispropile.user_id)
    thisobj=get_object_or_404(ApplyTask, task=thistask, submitter=thissubmitter)
    thisobj.approved=1
    thisobj.save()
    return render(request, 'Approve.html', context={'obj':thisobj})


def csv_list(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    data_types = RawDataType.objects.filter(task=task).distinct()	
    uploaded_files = RawDataSeqFile.objects.filter(raw_data_type__in=data_types).order_by('round')
    return render(request, 'csv_list.html', context={'task':task, 'file':uploaded_files})


def download(request, task_id):
    task_schema = TaskSchema.objects.filter(task_id=task_id).first()
    data=pd.read_sql_table(name=task_schema.TaskDataTableName)
    data.to_csv(r'/home/seonyeong/', index=False)
    messages.success('Download Completed')
    return HttpResponse("DOWNLOAD")
