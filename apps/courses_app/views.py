from django.shortcuts import render, redirect
from .models import Course, Description
# Create your views here.
def index(request):
    context = {
    "courses" : Course.objects.all(),
    "descriptions" : Description.objects.all()
    }
    if context is None:
        return render(request, "courses_app/index.html")
    else:
        return render(request, "courses_app/index.html", context)

def add(request):
    course = Course.objects.create(name=request.POST['name'])
    Description.objects.create(description=request.POST['description'], course=course)
    return redirect('/')

def remove(request, id):
    course = Course.objects.get(id=id)
    description = Description.objects.get(course=course)
    context = {
    "name" : course.name,
    "description": description.description,
    "id": course.id
    }
    return render(request, "courses_app/confirm.html", context)

def no(request):
    return redirect ('/')

def yes(request, id):
    course = Course.objects.get(id=id)
    description = Description.objects.get(course=course)
    course.delete()
    description.delete()
    return redirect('/')
