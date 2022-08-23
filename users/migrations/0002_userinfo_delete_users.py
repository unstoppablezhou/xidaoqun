# Generated by Django 4.1 on 2022-08-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userEmail', models.EmailField(max_length=32, verbose_name='邮箱')),
                ('userName', models.CharField(max_length=32, verbose_name='名称')),
                ('passWord', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]