# Generated by Django 3.2.2 on 2021-05-10 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_user', '0005_auto_20210510_0752'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]