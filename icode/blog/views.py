from django.shortcuts import render , HttpResponse , redirect
from blog.models import Post, PostComment
from django.contrib import messages
from blog.templatetags import getDict   
# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    # print(allPost)
    context = {'allPost':allPost}
    return render(request,'blog/blog.html',context)

    
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    # print("post",post)
    cmnt = PostComment.objects.filter(post=post,parent=None)
    replies = PostComment.objects.filter(post=post).exclude(parent=None)    
    usr = request.user
    # print("reply",replies)
    # print("commentss",cmnt)
    repliesDict = {}
    for reply in replies:
        if reply.parent.sno not in repliesDict.keys():
            repliesDict[reply.parent.sno] = [reply]
        else:
            repliesDict[reply.parent.sno].append(reply)
    # print("repliesDict",repliesDict)
    context = {"post":post,"comments":cmnt,"user":usr, "replyDict":repliesDict}
    return render(request,'blog/blogpost.html',context)

def commentPost(request):
    user = request.user
    comment = request.POST.get("comment")
    postsno = request.POST.get("postsno")
    post = Post.objects.get(sno=postsno)
    parentsno = request.POST.get("parentSno")
    # print(pare)
    if parentsno == "":
        comment = PostComment(user=user,comment=comment,post=post)
        comment.save()
        messages.success(request,"comment posted!!")
    else:
        parent = PostComment.objects.get(sno=parentsno)
        comment = PostComment(user=user,comment=comment,post=post,parent=parent)
        comment.save()
        messages.success(request,"reply posted!!")
    return redirect(f"/blog/{post.slug}")