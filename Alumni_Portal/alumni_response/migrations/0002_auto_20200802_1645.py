# Generated by Django 3.0.8 on 2020-08-02 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alumni_response', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='alumni',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='response', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='response',
            name='current_status',
            field=models.CharField(choices=[('Higher studies', 'Higher studies'), ('Job', 'Job'), ('Entrepreneurship', 'Entrepreneurship')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='response',
            name='passout_year',
            field=models.IntegerField(null=True),
        ),
    ]