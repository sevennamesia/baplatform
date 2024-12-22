# Generated by Django 2.2.12 on 2022-11-10 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0009_assignmentcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='baweb.Course', verbose_name='被选课程')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_student', to='baweb.StudentInfo', verbose_name='选课学生')),
            ],
        ),
    ]
