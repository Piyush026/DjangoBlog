from django.shortcuts import render , HttpResponse
from .models import Contact
from django.contrib import messages
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