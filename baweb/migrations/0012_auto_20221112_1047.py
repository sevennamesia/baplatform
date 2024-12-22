# Generated by Django 2.2.12 on 2022-11-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0011_assignmentsubmit'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmit',
            name='marks',
            field=models.SmallIntegerField(default=0, verbose_name='获得分数'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='max_marks',
            field=models.SmallIntegerField(default=100, verbose_name='最大分数'),
        ),
        migrations.AddField(
            model_name='assignmentsubmit',
            name='submit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
