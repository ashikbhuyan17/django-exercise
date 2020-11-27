# Generated by Django 2.2.13 on 2020-11-15 07:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0007_auto_20201114_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('bangla', 'bangla'), ('eng', 'eng'), ('urdu', 'urdu'), ('hindi', 'hindi')], default='bangla', max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='tuition/images'),
        ),
    ]