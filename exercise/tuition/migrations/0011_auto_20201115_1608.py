# Generated by Django 2.2.13 on 2020-11-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0010_auto_20201115_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='postviewtemp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='tuition/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]