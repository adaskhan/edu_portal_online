from rest_framework import serializers

from main.models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        # fields = '__all__'
        exclude = ['course_logo', ]


class LessonSerializer():
    pass