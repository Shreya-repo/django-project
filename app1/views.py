from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Students,Teachers
from .forms import PostForm
from django.shortcuts import redirect


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


def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app1/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app1/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'app1/post_edit.html', {'form': form})
    


def student_detail(request, pk):
    Students.objects.get(pk=pk)
    st = get_object_or_404(Students, pk=pk)
    return render(request, 'app1/student_detail.html', {'st': st})

def student_new(request):
    form = StudentForm()
    return render(request, 'app1/student_edit.html', {'form': form})

