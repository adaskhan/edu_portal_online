from django.shortcuts import render, redirect
from django.urls import reverse

from . import models


# Create your views here.
def index_page(request):
    print("request is accepted")
    # QuerySet - lazy
    favorite_courses = models.Course.objects.all()[:10]

    context = {
        "username": "Test",
        "favorite_courses": favorite_courses
    }
    return render(request, "main/index.html", context)


def login_page(request):
    return render(request, "main/login.html", {})


def courses_page(request):
    all_courses = models.Course.objects.all()
    return render(request, "main/courses.html", {"all_courses": all_courses})


def results_page(request):
    search_pattern = request.GET.get("course_name", None)
    if search_pattern and len(search_pattern) > 0:
        all_courses = models.Course.objects.filter(name__icontains=search_pattern[0])
    else:
        all_courses = models.Course.objects.all()
    return render(request, "main/courses.html", {"all_courses": all_courses})


def course_detail_page(request, pk):
    course = models.Course.objects.get(pk=pk)
    comments = models.Comment.objects.filter(course=course)

    if request.method == "GET":
        return render(request, "main/course_detail_page.html", {"course": course, "comments": comments})
    else:
        author = request.POST.get("author", None)
        comment_text = request.POST.get("comment", None)
        models.Comment.objects.create(
            author=author,
            comment_text=comment_text,
            course=course,
        )
        # POST - REDIRECT - GET
        return redirect(reverse("main:course_detail_page", args=(pk,)))


