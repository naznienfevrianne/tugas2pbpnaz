# Generated by Django 4.1 on 2022-09-28 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_alter_tasktodolist_date_alter_tasktodolist_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktodolist',
            name='date',
        ),
    ]
