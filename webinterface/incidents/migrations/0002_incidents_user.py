# Generated by Django 4.1 on 2022-08-16 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidents',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incidents', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
