from django.urls import path
from . import views

app_name = 'Lop'
urlpatterns = [
    path('show_class/', views.ShowClass, name='show_class'),
    path('add_class/', views.addClass.as_view(), name='add_class'),
    path('class/<int:id_class>/', views.detail_class, name='detail_class'),
    path('delete/<int:id_class>/', views.delete_class, name='delete_class'),
    path('update_class/<int:id_class>/',
         views.update.as_view(), name='update_class'),
]
