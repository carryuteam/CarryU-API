# Generated by Django 2.2.4 on 2019-10-01 16:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('openid', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='微信openid唯一标识符')),
                ('nickName', models.CharField(max_length=30, null=True, verbose_name='昵称')),
                ('avatarUrl', models.URLField(default='http://carryu.com', null=True, verbose_name='头像链接')),
                ('description', models.TextField(default='', verbose_name='描述信息')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='上次登陆时间')),
                ('school', models.IntegerField(null=True, verbose_name='学院')),
                ('gender', models.IntegerField(default=2, verbose_name='性别')),
                ('grade', models.IntegerField(null=True, verbose_name='年级')),
                ('coin', models.IntegerField(default=10, verbose_name='金币')),
                ('sessionKey', models.TextField(verbose_name='SessionKey')),
                ('password', models.TextField(verbose_name='供admin登陆密码')),
                ('username', models.TextField(verbose_name='复写先前的username')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
