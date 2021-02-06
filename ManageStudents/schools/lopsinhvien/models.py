from django.db import models

# Create your models here.


class Lop(models.Model):
    name_class = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=100)

    def __str__(self):
        return self.name_class


class Student(models.Model):
    lop = models.ForeignKey(Lop, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_student = models.CharField(max_length=50)
    detail_per = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
