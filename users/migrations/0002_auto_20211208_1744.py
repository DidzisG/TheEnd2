# Generated by Django 3.2.9 on 2021-12-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='grades',
            field=models.CharField(default='xx', max_length=100),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(default='xx', max_length=100),
        ),
    ]
