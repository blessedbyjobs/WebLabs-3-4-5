import random
from operator import attrgetter

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from datetime import date

from app.forms import SubjectForm
from app.models import ExamMark, Student


def lab_3(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['hour'] > 0:
                subject = form.save(commit=False)
                subject.name = form.cleaned_data['name']
                subject.hour = form.cleaned_data['hour']
                subject.semester = random.randint(1, 12)
                subject.save()
    else:
        form = SubjectForm()
    return render(request, 'main/lab_3.html', {'form': form})


def lab_4(request):
    students = Student.objects.all()
    max_date = date.today()
    max_date = max_date.replace(year=max_date.year - 20)
    result = Student.objects.values('birthday', 'name', 'surname').filter(birthday__gte=max_date)
    print(result)
    context = {
        'students': students,
        'result': result
    }
    template = loader.get_template('main/lab_4.html')
    return HttpResponse(template.render(context, request))


def lab_5(request):
    all_students = Student.objects.all()
    result = ExamMark.objects.values('student__university_id', 'subject__semester', 'subject__name', 'student__surname',
                                     'student__name', 'mark') \
        .filter(mark=5).order_by('student__university_id', 'subject__semester')
    print(result)
    context = {
        'all_students': all_students,
        'result': result
    }
    template = loader.get_template('main/lab_5.html')
    return HttpResponse(template.render(context, request))
