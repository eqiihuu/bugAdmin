import time, xlwt, StringIO
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .forms import CreateStageForm, CreateBugForm
from .models import Bug, Stage

def detail(request, bug_id):
    try:
        bug = Bug.objects.get(pk=bug_id)
        if request.method == 'POST':  #
            form = CreateStageForm(request.POST)  #
            if form.is_valid():  #
                action = request.POST.get('action',)
                if action == 'Update':
                    status = form.cleaned_data['status']
                    update_person = form.cleaned_data['update_person']
                    update_time = time.strftime('%Y-%m-%d %H:%M:%S')
                    bug = Bug.objects.get(pk=bug_id)
                    new_stage = Stage(status=status, update_person=update_person, update_time=update_time)
                    bug.stage_set.add(new_stage)
                    msg = 'New stage added!'+'\t'+str(new_stage.status)+','+str(new_stage.update_person)+','+str(new_stage.update_time)
                    latest_stage_list = bug.stage_set.order_by('-update_time')
                    return render(request, 'bugs/detail.html', {'bug': bug, 'stages': latest_stage_list, 'form': form, 'msg': msg})
        else:
            form = CreateStageForm()
    except Bug.DoesNotExist:
        raise Http404("Bug does not exist")
    latest_stage_list = bug.stage_set.order_by('-update_time')
    return render(request, 'bugs/detail.html', {'bug': bug, 'stages': latest_stage_list, 'form': form})


def base(request):
    if request.method == 'POST':
        form = CreateBugForm(request.POST)
        action = request.POST.get('action',)
        if form.is_valid():
            if action == 'Create':
                response = CreateBug(request, form)
                return response
            elif action == 'search':
                response = Search(request, form)
                return response
            elif action == 'delete?':
                response = DeleteBug(request, form)
                return response
            elif action == 'Save Excel':
                response = SaveExcel(request)
                return response
    else:
        form = CreateBugForm()
    latest_bug_list = Bug.objects.order_by('-create_time')
    return render(request, 'bugs/base.html', {'latest_bug_list': latest_bug_list, 'form': form})

def CreateBug(request, form):
    problem = form.cleaned_data['problem']
    create_person = form.cleaned_data['create_person']
    create_time = time.strftime('%Y-%m-%d %H:%M:%S')   # form.cleaned_data['time']
    new_bug = Bug(problem=problem, create_person=create_person, create_time=create_time)
    new_bug.save()
    msg = 'New Bug added!'+'\t'+str(new_bug.problem)+','+str(new_bug.create_person)+','+str(new_bug.create_time)
    # js_part = '<script>\nalert(\"'+msg+';\n</script>'
    latest_bug_list = Bug.objects.order_by('-create_time')
    return render(request, 'bugs/base.html', {'latest_bug_list': latest_bug_list, 'form': form, 'msg': msg})

def Search(request, form):
    content = form.cleaned_data['search_content']
    bugs = Bug.objects.filter(problem__icontains=content) | Bug.objects.filter(create_person__icontains=content)
    return render(request, 'bugs/base.html', {'latest_bug_list': bugs, 'form': form})

def DeleteBug(request, form):
    msg = 'Bug deleted!'
    for bug_id in request.POST.getlist('delete'):
        bug = Bug.objects.get(pk=bug_id)
        bug_msg = '\n'+str(bug.problem)+','+str(bug.create_person)+','+str(bug.create_time)
        bug.delete()
        msg += bug_msg
    latest_bug_list = Bug.objects.order_by('-create_time')
    return render(request, 'bugs/base.html', {'latest_bug_list': latest_bug_list, 'form': form, 'msg': msg})

def SaveExcel(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=BugList_'+time.strftime('%Y%m%d%H%M%S')+'.xls'
    wb = xlwt.Workbook(encoding = 'utf-8')
    sheet = wb.add_sheet(u'Bugs')
    #1st line
    sheet.write_merge(0, 0, 0, 4, 'Bug List')
    sheet.write(1,0, 'Bug ID')
    sheet.write(1,1, 'Problem')
    sheet.write(1,2, 'Create Person')
    sheet.write(1,3, 'Create Time')
    sheet.write(1,4, 'Note')
    row = 2
    for bug in Bug.objects.all():
        sheet.write(row,0, bug.id)
        sheet.write(row,1, bug.problem)
        sheet.write(row,2, bug.create_person)
        sheet.write(row,3, str(bug.create_time))
        sheet.write(row,4, bug.note)
        row=row + 1

    output = StringIO.StringIO()
    wb.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response