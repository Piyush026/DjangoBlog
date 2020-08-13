from django.shortcuts import render , HttpResponse
from blog.models import Post
# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    print(allPost)
    context = {'allPost':allPost}
    return render(request,'blog/blog.html',context)

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    print(post)
    context = {"post":post}
    # return HttpResponse(f'this is your blog post here: {slug}')
    return render(request,'blog/blogpost.html',context)