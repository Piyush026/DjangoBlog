from django.shortcuts import render , HttpResponse, redirect, HttpResponseRedirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post
from django.db import IntegrityError

# Create your views here.

def index(request):
    
    return render(request,'home/home.html')

def contact(request):
    # messages.error(request,"welcome to Contact")
    if request.method == 'POST':    
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        msg=request.POST['content']
        if len(name)<5 or len(phone)<10 or len(email)<10 or len(msg)<10:
            messages.error(request,"please fill Form correctly")

        else:
            contact = Contact(name=name,phone=phone,email=email,content=msg)
            messages.success(request,"form submited")
            contact.save()
    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')

def search(request):
    query = request.GET["query"]
    searchPost = Post.objects.filter(tittle__icontains=query)
    searchContent = Post.objects.filter(content__icontains=query)
    search = searchPost.union(searchContent)
    if search:
        context = {"allPost":search,"query":query}
    elif len(query) > 50:
        data = "Data not found"
        context = {"query":data}
    else:
        data = "Data not found"
        context = {"query":data}
        messages.warning(request,"try another..")
    return render(request,'home/search.html',context)


def signup(request):
    try:
        if request.method=="POST":
            username = request.POST['username']
            name = request.POST['name']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']
            # validation
            if pass1 != pass2:
                messages.error(request,"password must be same and minimum 8 char")
                return HttpResponseRedirect('/')
            if len(pass1) < 8:
                messages.error(request,"password must be minimum 8 char")
                return HttpResponseRedirect('/')

            icoderUser = User.objects.create_user(username,email,pass1)
            icoderUser.first_name = username
            icoderUser.last_name  =  name
            icoderUser.save()
            messages.success(request,"User created successfully")
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("404 NOT FOUND")
    except IntegrityError:
        messages.error(request,"Username must be unique")
        return HttpResponseRedirect('/')
    except:
        return HttpResponse("404 NOT FOUND")
        # return render_to_response("template.html", {"message": e.message})


def userlogin(request):
    if request.method=='POST':
        Uname = request.POST['Uname']
        loginpass = request.POST['loginpass']

        user =  authenticate(username=Uname,password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully")
            return redirect('home')
        else:
            messages.error(request,"invalid login")
            return redirect('home')
    return HttpResponse("404 not found")



def userlogout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('home')