from rest_framework import viewsets

from main.models import Course

from . import serializers


class CourseModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = serializers.CourseSerializer


class LessonViewSet():
    pass