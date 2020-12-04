from django.shortcuts import render, get_object_or_404
from submitter.models import Submitter
from raw_data.models import RawDataType, RawDataSeqFile
from task.models import Task
from rater.models import Rater, AssignedTask
from parsed_data.models import ParsedData
from rater.forms import RateForm
import random
import pandas as pd
import numpy as np
import json


# Create your views here.

def assigned_landing_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            raw_seqfile_pk = request.session.get('rawdataseqfile')
            null_tuple_num = request.session.get('num_null')

            rater = get_object_or_404(Rater, pk=request.user.user_id)
            raw_data_seq_file = RawDataSeqFile.objects.get(pk=raw_seqfile_pk)
            submitter = raw_data_seq_file.submitter
            task = raw_data_seq_file.raw_data_type.task
            total_tuple_num = request.session.get('num_row')
            duplicate_tuple_num = request.session.get('num_dup')
            column_null_ratio = null_tuple_num / total_tuple_num
            quantity_score = 10
            quality_score = form.data['quality_score']
            evaluated = 1
            pass_or_not = form.data['pass_or_not']

            rated = ParsedData.objects.create(rater=rater, raw_data_seq_file=raw_data_seq_file, submitter=submitter,
                                              task=task,
                                              total_tuple_num=total_tuple_num, duplicate_tuple_num=duplicate_tuple_num,
                                              column_null_ratio=column_null_ratio, quantity_score=quantity_score,
                                              quality_score=quality_score, evaluated=evaluated, pass_or_not=pass_or_not)
            rated.save()

            AssignedTask.objects.filter(rater=rater, raw_data=raw_data_seq_file).update(rated=1)

            #submitter score update
            scores=ParsedData.objects.filter(submitter=submitter).values_list('quality_score', flat=True)
            new_score=np.round(np.mean(scores),decimals=2)
            Submitter.objects.filter(user_id=submitter.user_id).update(score=new_score)

    else:
        rater = get_object_or_404(Rater, pk=request.user.user_id)

        if AssignedTask.objects.filter(rater=rater,rated=0).exists():
            pass
        else:
            items = RawDataSeqFile.objects.all()
            try:
                while True:
                    random_assigned = random.sample(list(items), 1)
                    if AssignedTask.objects.filter(rater=rater,raw_data=random_assigned[0]).exists() == False:
                         break

                raw_data_type = RawDataType.objects.filter(type_name=random_assigned[0].raw_data_type).first()

                a = raw_data_type.task.task_name
                task_info = Task.objects.filter(task_name=a).first()

                assigned_task = AssignedTask.objects.create(rater=rater, raw_data=random_assigned[0], task=task_info,
                                                            rated=0)
                assigned_task.save()
            except:
                pass

    not_rated = AssignedTask.objects.filter(rater=rater, rated=0)
    rated = AssignedTask.objects.filter(rater=rater, rated=1)
    info=""

    if len(rated) > 0:
        info = ParsedData.objects.filter(rater=rater)

    return render(request, "rater_landing.html", {"not_rated": not_rated, "rated": rated, "info": info})





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
    form = RateForm(request.POST)
    raw_data = RawDataSeqFile.objects.get(seqnumber=pk)
    csv_file = raw_data.file.open()
    data_html, scores = show_table_score(csv_file)
    request.session['rawdataseqfile'] = pk
    request.session['num_row'] = scores['num_row']
    request.session['num_dup'] = scores['num_dup']
    request.session['num_null'] = int(scores['num_null'].sum())  # 컬럼별 null ratio 계산 필요..

    return render(request, "rate.html", {"form": form, "raw_data": raw_data, "table": data_html, "scores": scores})


def rated(request):  # not used
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            raw_seqfile_pk = request.session.get('rawdataseqfile')
            null_tuple_num = request.session.get('num_null')

            rater = get_object_or_404(Rater, pk=request.user.user_id)
            raw_data_seq_file = RawDataSeqFile.objects.get(pk=raw_seqfile_pk)
            submitter = raw_data_seq_file.submitter
            task = raw_data_seq_file.raw_data_type.task
            total_tuple_num = request.session.get('num_row')
            duplicate_tuple_num = request.session.get('num_dup')
            column_null_ratio = null_tuple_num / total_tuple_num
            quantity_score = 10
            quality_score = form.data['quality_score']
            evaluated = 1
            pass_or_not = form.data['pass_or_not']

            rated = ParsedData.objects.create(rater=rater, raw_data_seq_file=raw_data_seq_file, submitter=submitter,
                                              task=task,
                                              total_tuple_num=total_tuple_num, duplicate_tuple_num=duplicate_tuple_num,
                                              column_null_ratio=column_null_ratio, quantity_score=quantity_score,
                                              quality_score=quality_score, evaluated=evaluated, pass_or_not=pass_or_not)
            rated.save()

            AssignedTask.object.filter(rater=rater, raw_data=raw_data_seq_file).update(rated=1)

            return render(request, "rater_landing.html", )

    else:
        form = RateForm(request.POST)
