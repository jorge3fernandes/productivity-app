# Generated by Django 4.0.2 on 2022-02-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twelveWeekYear_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='goal',
        ),
        migrations.AddField(
            model_name='goal',
            name='tag',
            field=models.ManyToManyField(to='twelveWeekYear_app.Tag'),
        ),
    ]
