from django.shortcuts import render, HttpResponse
from .models import Lop, Student
from django import views
from .forms import list_class_form, addStudent
# Create your views here.

# show list of classes in school


def ShowClass(request):
    return render(request, 'classes/Lopsinhvien.html', {'LS': Lop.objects.all()})

# add class into school


class addClass(views.View):
    def get(self, request):
        return render(request, 'classes/add_class.html', {"listClass": list_class_form})

    def post(self, request):
        new_class = list_class_form(request.POST)
        if new_class.is_valid():
            name_class = request.POST['name_class']
            descips = request.POST['descriptions']
            newClass = Lop(name_class=name_class, descriptions=descips)
            newClass.save()
            return render(request, 'classes/Lopsinhvien.html', {'LS': Lop.objects.all()})
        else:
            return HttpResponse('not valid')

# show option and list of student in class


def detail_class(request, id_class):
    cur_class = Lop.objects.get(pk=id_class)
    return render(request, 'classes/detail_class.html', {'Class': cur_class})

# delete this class and all student in class


def delete_class(request, id_class):
    cl = Lop.objects.get(pk=id_class)
    cl.delete()
    return render(request, 'classes/Lopsinhvien.html', {'LS': Lop.objects.all()})

# update info of class


class update_class(views.View):
    def get(self, request, id_class):
        return render(request, 'classes/add_class.html', {"listClass": list_class_form})

    def post(self, request, id_class):
        new_class = list_class_form(request.POST)
        if new_class.is_valid():
            name_class = request.POST['name_class']
            descips = request.POST['descriptions']
            dic_up = {"name_class": name_class, "descriptions": descips}
            obj = Lop.objects.get(pk=id_class)
            obj.__dict__.update(dic_up)
            obj.save()
            return render(request, 'classes/Lopsinhvien.html', {'LS': Lop.objects.all()})
        else:
            return HttpResponse('not valid')

# add student in class


class add_student(views.View):
    def get(self, request, id_class):
        SF = addStudent()
        return render(request, 'classes/add_student.html', {'sf': SF, 'class': Lop.objects.get(pk=id_class)})

    def post(self, request, id_class):
        my_class = Lop.objects.get(pk=id_class)
        stu = my_class.student_set.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            id_student=request.POST['id_student'],
            detail_per=request.POST['detail_per']
        )
        stu.save()
        return render(request, 'classes/detail_class.html', {'Class': my_class})

# show detail student


def detail_student(request, id_class, id_stu):
    cur_class = Lop.objects.get(pk=id_class)
    obj = cur_class.student_set.get(pk=id_stu)
    return render(request, 'classes/detail_student.html', {'Stu': obj, 'Cur_class': cur_class})

# delete this class and all student in class


def delete_student(request, id_class, id_stu):
    cl = Lop.objects.get(pk=id_class)
    student = cl.student_set.get(pk=id_stu)
    student.delete()
    return render(request, 'classes/detail_class.html', {'Class': cl})

# update info of student


class update_student(views.View):
    def get(self, request, id_class,id_stu):
        SF = addStudent()
        return render(request, 'classes/add_student.html', {'sf': SF, 'class': Lop.objects.get(pk=id_class)})

    def post(self, request, id_class,id_stu):
        my_class = Lop.objects.get(pk=id_class)
        stu = my_class.student_set.get(pk= id_stu)
        dic_up={
        "first_name":request.POST['first_name'],
        "last_name":request.POST['last_name'],
        "id_student":request.POST['id_student'],
        "detail_per":request.POST['detail_per']
        }
        stu.__dict__.update(dic_up)
        stu.save()
        return render(request, 'classes/detail_class.html', {'Class': my_class})