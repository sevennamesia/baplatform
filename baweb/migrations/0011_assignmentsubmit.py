# Generated by Django 2.2.12 on 2022-11-12 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0010_studentcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='submission/', verbose_name='任务文档')),
                ('file_name', models.CharField(blank=True, default=None, max_length=64, verbose_name='文档名')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submit_assignment', to='baweb.Assignment', verbose_name='所提交的任务')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignmentsubmit_student', to='baweb.StudentInfo', verbose_name='学生')),
            ],
        ),
    ]
