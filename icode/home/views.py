from django.shortcuts import render , HttpResponse
from .models import Contact
# Create your views here.

def index(request):
    
    return render(request,'home/home.html')

def contact(request):
    if request.method == 'POST':    
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        msg=request.POST['content']
        contact = Contact(name=name,phone=phone,email=email,content=msg)
        contact.save()
    return render(request,'home/contact.html')


def about(request):
    return HttpResponse("About")