# Generated by Django 3.2.3 on 2021-06-02 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_customuser_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.URLField(default=''),
        ),
    ]