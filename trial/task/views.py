from django.shortcuts import render
from task.models import Task
#from _mysql import connection
from django.http.response import HttpResponseRedirect

# Create your views here.

def ListFunc(request):
    data= Task.objects.all()
    return render(request, 'task_list.html', {'tasks':data})
	
def ApprovedTasks(request):
    task= Task.objects.all()
    return render(request, 'submitter_handing.html', {'task':task})