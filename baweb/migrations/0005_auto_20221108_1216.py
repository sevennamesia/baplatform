# Generated by Django 2.2.12 on 2022-11-08 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0004_auto_20221108_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='任务名')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='任务简介')),
                ('ddl', models.DateField(verbose_name='任务截止时间')),
            ],
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_profile_pic',
            field=models.ImageField(blank=True, upload_to='userimg/student_profile_pic', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='teacherinfo',
            name='teacher_profile_pic',
            field=models.ImageField(blank=True, upload_to='userimg/teacher_profile_pic', verbose_name='头像'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='课程名')),
                ('course_profile_pic', models.ImageField(blank=True, upload_to='userimg/course_profile_pic/', verbose_name='课程图')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='课程简介')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_teacher', to='baweb.TeacherInfo', verbose_name='教课老师')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='assignments/', verbose_name='任务文档')),
                ('file_name', models.CharField(blank=True, default=None, max_length=64, verbose_name='文档名')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_assignment', to='baweb.Assignment', verbose_name='所属任务')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_course', to='baweb.Course', verbose_name='所属课程'),
        ),
    ]