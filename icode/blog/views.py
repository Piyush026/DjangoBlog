from django.shortcuts import render , HttpResponse , redirect
from blog.models import Post, PostComment
from django.contrib import messages
# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    print(allPost)
    context = {'allPost':allPost}
    return render(request,'blog/blog.html',context)

    
def blogPost(request,slug):
    comment={}
    post = Post.objects.filter(slug=slug).first()
    # print("post",post)
    cmnt = PostComment.objects.filter(post=post)
    # print("commentss",cmnt)
    context = {"post":post,"comments":cmnt}
    return render(request,'blog/blogpost.html',context)

def commentPost(request):
    user = request.user
    comment = request.POST.get("comment")
    postsno = request.POST.get("postsno")
    post = Post.objects.get(sno=postsno)
    comment = PostComment(user=user,comment=comment,post=post)
    comment.save()
    messages.success(request,"comment posted!!")
    return redirect(f"/blog/{post.slug}")