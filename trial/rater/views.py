from django.shortcuts import render, get_object_or_404
from raw_data.models import RawDataType, RawDataSeqFile
from task.models import Task
from rater.models import Rater,AssignedTask
import random
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

def assigned_landing_view(request, *args, **kwargs):
    rater = get_object_or_404(Rater, pk=request.user.user_id)

    if AssignedTask.objects.filter(rater=rater).exists():
        print('object exists')
        assigned_task=AssignedTask.objects.filter(rater=rater)
        task_info = Task.objects.filter(task_id=assigned_task.task)

        return render(request, "rater_landing.html",
                      {"task_info": task_info , "assigned_task":assigned_task,"rater":rater})
    else:
        items = RawDataSeqFile.objects.all()
        random_assigned= random.sample(list(items), 1)
        raw_data_type = RawDataType.objects.filter(type_name=random_assigned[0].raw_data_type).first()
        a= raw_data_type.task.task_name
        task_info = Task.objects.filter(task_name=a).first()

        assigned_task = AssignedTask.objects.create(rater=rater, raw_data=random_assigned[0], task=task_info)
        assigned_task.save()

        return render(request, "rater_landing.html",
                      {"task_info": task_info, "assigned_task": items, "rater":rater})

