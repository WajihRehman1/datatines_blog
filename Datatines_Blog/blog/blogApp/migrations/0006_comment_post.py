# Generated by Django 3.0.8 on 2020-07-16 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0005_auto_20200716_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Post',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogApp.post'),
            preserve_default=False,
        ),
    ]
