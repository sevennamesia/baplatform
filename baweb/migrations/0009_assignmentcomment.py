# Generated by Django 2.2.12 on 2022-11-10 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baweb', '0008_auto_20221110_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='任务评价')),
                ('created_at', models.DateField(auto_now=True, verbose_name='评价时间')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_assignment', to='baweb.Assignment', verbose_name='所属任务')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='baweb.User', verbose_name='评价人')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]