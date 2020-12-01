from django.shortcuts import render, get_object_or_404
from raw_data.models import RawDataType, RawDataSeqFile
from task.models import Task
from rater.models import Rater, AssignedTask
from parsed_data.models import ParsedData
import random
import pandas as pd


# Create your views here.

def assigned_landing_view(request, *args, **kwargs):
    rater = get_object_or_404(Rater, pk=request.user.user_id)

    if AssignedTask.objects.filter(rater=rater).exists():
        pass
    else:
        items = RawDataSeqFile.objects.all()

        while True:
            random_assigned = random.sample(list(items), 1)
            if AssignedTask.objects.filter(raw_data=random_assigned[0]).exists()==False:
                break

        raw_data_type = RawDataType.objects.filter(type_name=random_assigned[0].raw_data_type).first()


        a = raw_data_type.task.task_name
        task_info = Task.objects.filter(task_name=a).first()

        assigned_task = AssignedTask.objects.create(rater=rater, raw_data=random_assigned[0], task=task_info, rated=0)
        assigned_task.save()

    not_rated = AssignedTask.objects.filter(rater=rater, rated=0)
    rated = AssignedTask.objects.filter(rater=rater, rated=1)

    return render(request, "rater_landing.html", {"not_rated": not_rated, "rated": rated})


def show_table_score(file):
    data = pd.read_csv(file)
    data_html = data.to_html()
    score = calculate_auto_score(data)
    return data_html, score


def calculate_auto_score(data):
    """
    각 파싱 데이터 시퀀스 파일은 전체 튜플 수, 중복 튜플 수, Column 별 Null 속성 비율 과 같은 정성평가 지표 결과를 갖고 있다.
    """
    row_num = data.shape[0]
    duplicateRowsDF = data[data.duplicated()]
    dup = duplicateRowsDF.shape[0]
    null_column = data.isnull().sum(axis=0)

    return {"num_row": row_num, "num_dup": dup, "num_null": null_column}


def rater_rates(request, pk):
    raw_data = RawDataSeqFile.objects.get(seqnumber=pk)
    csv_file = raw_data.file.open()
    data_html, scores = show_table_score(csv_file)

    return render(request, "rate.html", {"raw_data": raw_data, "table": data_html, "scores": scores})
