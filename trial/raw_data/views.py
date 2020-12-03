from django.shortcuts import render, redirect
from .forms import DataTypeForm, DataTypeSchemaForm
from .models import RawDataType, RawDataTypeSchema
# Create your views here.

def createdatatype(request):
    if request.method == 'POST':
        form = DataTypeForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.save()
            return redirect('createtypeschema')
    else:
        form = DataTypeForm()
    return render(request, 'createdatatype.html', {'form': form})

def createtypeschema(request):
    if request.method == 'POST':
        form = DataTypeSchemaForm(request.POST)

        if form.is_valid():
            user_instance = form.save(commit=False)
            user_instance.save()
            return redirect('createtypeschema')
    else:
        form = DataTypeSchemaForm()
    return render(request, 'createtypeschema.html', {'form': form})

def datatypelist(request):
    datatype = RawDataType.objects.all()
    typefield = RawDataTypeSchema.objects.all()
    return render(request, "datatypelist.html", {"datatype": datatype, "typefield": typefield})

##def type_detail(request, pk):
   ## type = RawDataTypeSchema.objects.get(pk=pk)
 ##   return render(request, 'type_detail.html', {'type': type})