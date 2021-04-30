from django.shortcuts import render
from django.utils import timezone
from .models import Post,Students,Teachers

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app1/post_list.html', {'posts': posts})

def students_list(request):
    stu = Students.objects.all()
    return render(request, 'app1/students_list.html', {'stu': stu})

def teachers_list(request):
    teach = Teachers.objects.all()
    return render(request, 'app1/teachers_list.html', {'teach': teach})