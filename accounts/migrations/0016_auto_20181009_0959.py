# Generated by Django 2.0.6 on 2018-10-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20181008_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='avatars/anonymous.png', upload_to='avatars'),
        ),
    ]
