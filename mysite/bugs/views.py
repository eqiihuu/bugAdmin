import time
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from django import forms
from .forms import CreateStageForm, CreateBugForm
from .models import Bug, Stage

def detail(request, bug_id):
    try:
        bug = Bug.objects.get(pk=bug_id)
        stages = bug.stage_set.all()
        if request.method == 'POST':  #
            form = CreateStageForm(request.POST)  #
            if form.is_valid():  #
                status = form.cleaned_data['status']
                update_person = form.cleaned_data['person']
                update_time = time.strftime('%Y-%m-%d %H:%M:%S')   # form.cleaned_data['time']
                bug = Bug.objects.get(pk=bug_id)
                new_stage = Stage(status=status, update_person=update_person, update_time=update_time)
                bug.stage_set.add(new_stage)
                msg = 'New stage added!'+ '\n'+str(new_stage.status)+','+str(new_stage.person)+','+str(new_stage.time)
                return HttpResponse(msg)
        else:
            form = CreateStageForm()
        return render(request, 'bugs/detail.html', {'bug': bug, 'stages': stages, 'form': form})
    except Bug.DoesNotExist:
        raise Http404("Bug does not exist")
    return render(request, 'bugs/detail.html', {'bug': bug, 'stages': stages})


def base(request):
    if request.method == 'POST':
        form = CreateBugForm(request.POST)
        if request.POST.getlist('Create'):
            if form.is_valid():  #
                problem = form.cleaned_data['problem']
                create_person = form.cleaned_data['create_person']
                create_time = time.strftime('%Y-%m-%d %H:%M:%S')   # form.cleaned_data['time']
                new_bug = Bug(problem=problem, create_person=create_person, create_time=create_time)
                new_bug.save()
                msg = 'New Bug added!'+'<br>'+str(new_bug.problem)+','+str(new_bug.create_person)+','+str(new_bug.create_time)+'<br>'
                return HttpResponse(msg)
        if request.POST.getlist('delete?'):
            if form.is_valid():  #
                msg = 'Bug deleted!'
                for bug_id in request.POST.getlist('delete'):
                    bug = Bug.objects.get(pk=bug_id)
                    bug_msg = '<br>'+str(bug.problem)+','+str(bug.create_person)+','+str(bug.create_time)+'<br>'
                    bug.delete()
                    msg += bug_msg
                return HttpResponse(msg)
    else:
        form = CreateBugForm()
    latest_bug_list = Bug.objects.order_by('-create_time')
    return render(request, 'bugs/base.html', {'latest_bug_list': latest_bug_list, 'form': form})

