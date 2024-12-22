# Generated by Django 2.2.12 on 2022-12-01 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0012_auto_20221112_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='组名')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_course', to='baweb.Course', verbose_name='所属课程')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_head', models.BooleanField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupmember_group', to='baweb.Group', verbose_name='所属小组')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupmember_student', to='baweb.StudentInfo', verbose_name='小组成员')),
            ],
        ),
    ]
