from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    lessons_count = models.IntegerField(verbose_name='Количество уроков')
    lesson_duration = models.FloatField(verbose_name='Количество минут для одного урока')
    course_logo = models.ImageField(verbose_name='Логотип')

    def __str__(self):
        return f"{self.name}: {self.description}"


class Student(models.Model):
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.date_of_birth}: {self.course}"


class Comment(models.Model):
    author = models.CharField(max_length=30, verbose_name='Автор комментария')
    comment_text = models.TextField(verbose_name='Текст комментария')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания комментария')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author}: {self.created_date} - {self.course}"
