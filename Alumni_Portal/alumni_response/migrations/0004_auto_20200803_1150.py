# Generated by Django 3.0.3 on 2020-08-03 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_response', '0003_auto_20200802_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='current_status',
            new_name='post_college',
        ),
    ]