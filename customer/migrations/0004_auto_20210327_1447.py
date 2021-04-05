# Generated by Django 3.1.4 on 2021-03-27 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210324_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='msg',
            field=models.CharField(max_length=100),
        ),
    ]