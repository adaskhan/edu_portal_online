from django.db import models


class Course(models.Model):
    pass


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)