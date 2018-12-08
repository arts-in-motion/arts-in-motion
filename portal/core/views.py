
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from portal.classes.models import Class
from portal.contacts.models import Student
from django.contrib.auth.decorators import login_required

@login_required
def class_reports(request):
    classes = Class.objects.all()
    return render(request,'core/class_reports.html',{'classes': classes})

@login_required
def detail_class_reports(request, class_id):
    aim_class = get_object_or_404(Class, pk=class_id)
    students = Student.objects.filter(classes__in=[aim_class])
    return render(request, 'core/detail_class_reports.html', {'class': aim_class, 'students': students})