from django.shortcuts import render , HttpResponse

# Create your views here.

def blogHome(request):
    return HttpResponse("MY Blog")

def blogPost(request,slug):
    return HttpResponse(f'this is your blog post here: {slug}')