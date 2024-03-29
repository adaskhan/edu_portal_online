# Generated by Django 4.0.6 on 2022-07-20 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('lessons_count', models.IntegerField(verbose_name='Количество уроков')),
                ('lesson_duration', models.FloatField(verbose_name='Количество минут для одного урока')),
                ('course_logo', models.ImageField(upload_to='', verbose_name='Логотип')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.course')),
            ],
        ),
    ]
