from django.shortcuts import render, HttpResponse
from .models import Lop
from django import views
from .forms import list_class_form
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


class update(views.View):
    def get(self, request):
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
            return render(request, 'classes/detail_class.html', {'Class': Lop.objects.get(pk=id_class)})
        else:
            return HttpResponse('not valid')

#add student in class