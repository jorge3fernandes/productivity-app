# Generated by Django 4.0.2 on 2022-02-06 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twelveWeekYear_app', '0003_remove_goal_tag_goal_tags_delete_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='week',
            old_name='tactit',
            new_name='tactic',
        ),
    ]
