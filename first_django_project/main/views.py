from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("This is my response!")

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def show(request, my_val):
    return HttpResponse(f"placeholder to display blog number: {my_val}")

def edit(request, my_val):
    return HttpResponse(f"placeholder to edit blog number: {my_val}")

def destroy(request, my_val):
    return index(request)