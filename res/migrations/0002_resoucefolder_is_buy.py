# Generated by Django 2.2.4 on 2019-10-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('res', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resoucefolder',
            name='is_buy',
            field=models.IntegerField(default=0),
        ),
    ]
