from django.urls import path
from . import views

urlpatterns = [
    path('students-list', views.students_list, name='students_list'),
    path('teachers-list', views.teachers_list, name='teachers_list'),
    path('', views.post_list, name='post_list'),

]