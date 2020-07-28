# Generated by Django 3.0.8 on 2020-07-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Post',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
