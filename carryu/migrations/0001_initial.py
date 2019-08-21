# Generated by Django 2.2.4 on 2019-08-21 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resid', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=50)),
                ('resURL', models.URLField()),
                ('school', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('picURLs', models.TextField()),
                ('description', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', models.TextField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('openid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nickName', models.CharField(max_length=30)),
                ('avatarUrl', models.URLField()),
                ('description', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('school', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('coin', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ResouceFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField()),
                ('resid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carryu.Resource')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carryu.User')),
            ],
            options={
                'unique_together': {('userid', 'resid')},
            },
        ),
    ]
