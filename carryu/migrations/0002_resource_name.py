# Generated by Django 2.2.4 on 2019-08-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carryu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='name',
            field=models.CharField(default='res', max_length=50),
        ),
    ]