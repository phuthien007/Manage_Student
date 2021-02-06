from django.urls import path
from . import views

app_name = 'Lop'
urlpatterns = [
    path('show_class/', views.ShowClass, name='show_class'),
    path('add_class/', views.addClass.as_view(), name='add_class'),
    path('class/<int:id_class>/', views.detail_class, name='detail_class'),
    path('delete/<int:id_class>/', views.delete_class, name='delete_class'),
    path('update_class/<int:id_class>/',
         views.update_class.as_view(), name='update_class'),
    path('class/<int:id_class>/add_student',
         views.add_student.as_view(), name='add_student'),
    path('class/<int:id_class>/student_detail/<int:id_stu>',
         views.detail_student, name='detail_student'),
    path('class/<int:id_class>/student_delete/<int:id_stu>',
         views.delete_student, name='delete_student'),
    path('class/<int:id_class>/student_update/<int:id_stu>',
         views.update_student.as_view(), name='update_student'),
]
