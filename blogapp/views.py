from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog
from .models import Pictures

# Create your views here.
def welcome(request):
    return render(request, 'blog/index.html')

def home(request):
    blogs = Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    picture = Pictures.objects
    return render(request, 'blog/home.html',{'blogs':blogs, 'posts':posts, 'picture':picture})

def create(request):
    #새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == "POST":
        #입력된 블로그 글들을 저장해라
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request,'blog/new.html', {'form':form})
    

def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == 'POST':
        form = NewBlog(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewBlog(instance= blog)
        return render(request, 'blog/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    #이용자가 원하는 몇번 객체
    
    return render(request, 'blog/detail.html', {'blog':blog})

def top(request):
    picture = Pictures.objects
    return render(request,'blog/top_detail.html', {'picture': picture})