from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    
    return render(request,'home/home.html')

def contact(request):
    return HttpResponse("Contact")


def about(request):
    return HttpResponse("About")