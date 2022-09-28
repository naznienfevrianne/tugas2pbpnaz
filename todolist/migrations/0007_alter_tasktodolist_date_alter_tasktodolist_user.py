# Generated by Django 4.1 on 2022-09-28 07:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todolist', '0006_alter_tasktodolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktodolist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 28, 14, 54, 20, 131505)),
        ),
        migrations.AlterField(
            model_name='tasktodolist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
