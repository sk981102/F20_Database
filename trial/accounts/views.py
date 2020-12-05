from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm, CheckPasswordForm, ChangeInfoForm
from django.contrib.auth.forms import PasswordChangeForm
#from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.hashers import check_password
from django.urls import path
from django.db.models import Q
from submitter.models import Submitter
from task.models import ApplyTask, Task
from rater.models import Rater
from parsed_data.models import ParsedData
from raw_data.models import RawDataSeqFile, RawDataType
from django.db.models import Count

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            #user_instance.generate()
            user_instance.set_password(form.cleaned_data['PW'])
            user_instance.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['PW']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def viewusers(request):
    num = UserProfile.objects.count()
    candidates = UserProfile.objects.all()
    context = {'candidates' : candidates, 'num':num}
    return render(request, 'viewusers.html', context)

def myaccount(request):
    form = get_object_or_404(UserProfile, pk=request.user.pk)
    return render(request, 'myaccount.html', {'form': form})

def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('myaccount')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepw.html', {'form': form})

def changeinfo(request):
    if request.method == 'POST':
        form = ChangeInfoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('myaccount')
    else:
        form = ChangeInfoForm(instance=request.user)
        return render(request, 'changeinfo.html', {'form': form})

def deleteaccount(request):

    if request.method == 'POST':
        password_form = CheckPasswordForm(request.user, request.POST)

        if password_form.is_valid():
            request.user.delete()
            logout(request)
            messages.success(request, "회원탈퇴가 완료되었습니다.")
            return redirect('login')
    else:
        password_form = CheckPasswordForm(request.user)

    return render(request, 'deleteaccount.html', {'password_form': password_form})

def search(request):
    blogs = None
    q = None
    if 'q' in request.GET:
        q = request.GET.get('q')
        blogs = UserProfile.objects.all().filter(Q(username__contains=q) | Q(gender__contains=q) | Q(birthdate__contains=q))
        return render(request, 'search.html', {'blogs': blogs, 'q': q})

    else:
        return render(request, 'search.html')


def post_detail(request, pk):
    request.session['submitter_id'] = pk
    post = UserProfile.objects.get(pk=pk)
    if post.role == 'S':
        submitter = get_object_or_404(Submitter,pk=pk)                              #15
        raw = RawDataSeqFile.objects.filter(submitter=submitter).values_list('seqnumber',flat=True)  # 원본데이터시퀀스 파일 오브젝트 RawDataSeqFile object (1) RawDataSeqFile object (2) RawDataSeqFile object (4) RawDataSeqFile object (11)
        parsed = ParsedData.objects.filter(raw_data_seq_file__in=raw,pass_or_not=1).values_list('raw_data_seq_file',flat=True)
        rawfile = RawDataSeqFile.objects.filter(submitter=submitter,seqnumber__in=parsed)
        apply = ApplyTask.objects.filter(submitter=submitter, approved=1).values('task')  # <QuerySet [{'task': 1}, {'task': 2}, {'task': 3}]>

        tak1 = Task.objects.filter(task_id__in=apply)  # 제출자가 참여중인 태스크 목록.(승인 된 것들만)
        #temp = raw.values('seqnumber')  # 제출자가 제출한 파일 시퀀스number 오브젝트 {'seqnumber': 1}   {'seqnumber': 2}   {'seqnumber': 4}   {'seqnumber': 11}   {'seqnumber': 12}
        #pared = ParsedData.objects.filter(raw_data_seq_file__in=temp, pass_or_not=1)  # 제출자가 제출한 패쓰 된 paredData objects
        #temppared = pared.values('task').order_by('task').distinct()  #


        # task = tak1.filter(task_id__in=temppared)                   #제출자가 참여중인 목록 중
        #taktemp = tak1.values_list('task_id', flat=True)  # parsedtemp 에 현제 제출자가 참가해 있는 태스크들의 id를 넘겨 줌.
       # parsedtemp = pared.filter(task__in=taktemp).values_list('raw_data_seq_file',flat=True).distinct()  # 참가해있는 테이블들에 제출되어 진 파씽파일들
        #rawtemp = raw.filter(seqnumber__in=parsedtemp)  # 파씽파일들의 이름을 뽑기 위한 용도.

        #apply = ApplyTask.objects.filter(submitter=submitter).values('task')        #<QuerySet [{'task': 1}, {'task': 2}, {'task': 3}]>
      #  tak = Task.objects.filter(task_id__in=apply)                                #<QuerySet [<Task: 예금 및 적금 데이터>, <Task: 베스트셀러 데이터>, <Task: 수강신청 데이터>]>
      #  raw_data = RawDataSeqFile.objects.filter(submitter=submitter).values('file')#[{'file': 'bestsellers_with_categories.csv'}, {'file': 'fiction_correct.csv'}, {'file': 'fiction_incorrect.csv'}]>
      #  raw = RawDataType.objects.filter(task__in=tak).values('task').order_by('task').distinct()

       # parsed = get_object_or_404(ParsedData,pk=raw_data)

        context = {
            'post': post,#, 'apply': apply, 'submitter': submitter, 'tak': tak, 'parsed': raw_data, 'raw': raw

            'raw': rawfile,
            'apply': apply,
            'tak1': tak1,
           # 'pared': pared,
            # 'temp': temp,
           # 'temppared': temppared,
          #  'taktemp': taktemp,
          #  'parsedtemp': parsedtemp,
          #  'rawtemp': rawtemp
            # 'task': task
        }
        return render(request, 'post_detail.html', context)
    elif post.role == 'R':

        parsed = ParsedData.objects.filter(rater=pk).values_list('raw_data_seq_file',flat=True)#(rater=pk)
        raw = RawDataSeqFile.objects.filter(seqnumber__in=parsed)
        context = {
            'post':post, 'parsed': parsed, 'raw': raw
        }
        return render(request, 'post_detail.html', context)

    else:
        context = {
            'post': post
        }
        return render(request, 'post_detail.html', context)

#def Tasks(request):
 #   task = .objects.all()
  #  context = {'candidates' : candidates}
   # return render(request, 'viewusers.html', context)

def type_detail(request, pk):
    task = Task.objects.get(pk=pk)
    parsed =  ParsedData.objects.filter(task=pk,pass_or_not=1).values_list('raw_data_seq_file',flat=True)
    temp = request.session.get('submitter_id')
    temp1 = int(temp)
    raw = RawDataSeqFile.objects.filter(submitter=temp1,seqnumber__in=parsed)
    num = raw.count()
    #temp3= RawDataSeqFile.objects.filter(submitter=temp1)
    #temp4 = ParsedData.objects.all()
    #temp = parsed.values_list('raw_data_seq_file')
    #raw = RawDataSeqFile.objects.filter(submitter=15,seqnumber=temp)

    context= {
        'parsed': parsed,'temp':temp1, 'raw':raw, 'task':task, 'num':num#,'temp3':temp4
    }
    return render(request, 'type_detail.html', context)

#def test(request):
 #   raw = RawDataSeqFile.objects.filter(submitter=15)  # 원본데이터시퀀스 파일 오브젝트 RawDataSeqFile object (1) RawDataSeqFile object (2) RawDataSeqFile object (4) RawDataSeqFile object (11)   RawDataSeqFile object (12)
 #   temp = raw.values('seqnumber')  # 제출자가 제출한 파일 시퀀스number 오브젝트 {'seqnumber': 1}   {'seqnumber': 2}   {'seqnumber': 4}   {'seqnumber': 11}   {'seqnumber': 12}
 #   pared = ParsedData.objects.filter(raw_data_seq_file__in=temp, pass_or_not=1)  # 제출자가 제출한 패쓰 된 paredData objects
 #   temppared = pared.values('task').order_by('task').distinct()  #

  #  apply = ApplyTask.objects.filter(submitter=15, approved=1).values('task')  # <QuerySet [{'task': 1}, {'task': 2}, {'task': 3}]>
  #  tak1 = Task.objects.filter(task_id__in=apply)  # 제출자가 참여중인 태스크 목록.(승인 된 것들만)
    # task = tak1.filter(task_id__in=temppared)                   #제출자가 참여중인 목록 중
  #  taktemp = tak1.values_list('task_id', flat=True)  # parsedtemp 에 현제 제출자가 참가해 있는 태스크들의 id를 넘겨 줌.
  #  parsedtemp = pared.filter(task__in=taktemp).values_list('raw_data_seq_file',
  #                                                          flat=True).distinct()  # 참가해있는 테이블들에 제출되어 진 파씽파일들
  #  rawtemp = raw.filter(seqnumber__in=parsedtemp)  # 파씽파일들의 이름을 뽑기 위한 용도.


    #context = {
    ##    'temp': temp,
     #   'raw': raw,
     #   'apply': apply,
     #   'pared':pared,
     #   'tak1': tak1,
     #   'temppared': temppared,
     #   'taktemp':taktemp,
     #   'parsedtemp': parsedtemp,
     #   'rawtemp': rawtemp
     #   #'task': task
    #}
    #return render(request, 'type_detail.html', context)

#def task_detail(request, pk):
#    task = Task.objects.get(pk=pk)
#    context={z
#        'task': task
#    }
#    return render(reqzuest,'task_detail',context)
#def test2(request):
#    test2 = RawDataType.objects.all()
#    test = UserProfile.objects.count()
#    test3 = ApplyTask.objects.filter(submitter=15).values('task')  # <QuerySet [{'task': 1}, {'task': 2}, {'task': 3}]>
#    test4 = Task.objects.filter(task_id__in=test3)
#    return render(request, 'test2.html', {'test2': test2 , 'test': test, 'test3': test3, 'test4': test4})