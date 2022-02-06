# Generated by Django 4.0.2 on 2022-02-06 11:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tactic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('frequency', models.CharField(blank=True, choices=[['daily', 'Daily'], ['weekly', 'Weekly'], ['once', 'Once']], default='once', max_length=50, null=True)),
                ('score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('goal', models.ManyToManyField(to='twelveWeekYear_app.Goal')),
            ],
        ),
        migrations.CreateModel(
            name='TwelveWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('victories_successes', models.TextField(blank=True, max_length=1000, null=True, verbose_name='What are you pleased with?')),
                ('breakdowns', models.TextField(blank=True, max_length=1000, null=True, verbose_name='What are you concerned about?')),
                ('actions', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Insigths and Actions for next week.')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('tactit', models.ManyToManyField(to='twelveWeekYear_app.Tactic')),
                ('twelve_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twelveWeekYear_app.twelveweek')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(blank=True, choices=[('physical', 'Physical'), ('spiritual', 'Spiritual'), ('work', 'Work')], max_length=200, null=True)),
                ('goal', models.ManyToManyField(to='twelveWeekYear_app.Goal')),
            ],
        ),
        migrations.AddField(
            model_name='goal',
            name='TwelveWeek',
            field=models.ManyToManyField(blank=True, to='twelveWeekYear_app.TwelveWeek'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reflection', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Reflection on the day!')),
                ('score', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('tactic', models.ManyToManyField(to='twelveWeekYear_app.Tactic')),
                ('twelve_week', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='twelveWeekYear_app.twelveweek')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twelveWeekYear_app.week')),
            ],
        ),
    ]