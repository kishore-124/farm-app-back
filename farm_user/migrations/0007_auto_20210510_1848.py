# Generated by Django 3.2.2 on 2021-05-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_user', '0006_auto_20210510_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, max_length=300, null=True, unique=True),
        ),
    ]
