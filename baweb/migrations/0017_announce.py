# Generated by Django 2.2.12 on 2023-01-10 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0016_coursecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField(verbose_name='通知')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_course', to='baweb.Course', verbose_name='所属课程')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_teacher', to='baweb.TeacherInfo', verbose_name='所属老师')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
