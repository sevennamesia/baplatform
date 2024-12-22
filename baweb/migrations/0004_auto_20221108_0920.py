# Generated by Django 2.2.12 on 2022-11-08 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0003_studentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Teacher', serialize=False, to='baweb.User', verbose_name='老师')),
                ('name', models.CharField(default='未知', max_length=64, verbose_name='名字')),
                ('gender', models.SmallIntegerField(blank=True, choices=[(1, '男'), (2, '女'), (3, '保密')], default=3, verbose_name='性别')),
                ('email', models.EmailField(blank=True, max_length=64, verbose_name='邮箱')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='手机号')),
                ('description', models.TextField(blank=True, max_length=1000, verbose_name='教师简介')),
                ('teacher_profile_pic', models.ImageField(blank=True, upload_to='../media/userimg/teacher_profile_pic', verbose_name='头像')),
            ],
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=64, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='name',
            field=models.CharField(default='未知', max_length=64, verbose_name='名字'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='手机号'),
        ),
    ]