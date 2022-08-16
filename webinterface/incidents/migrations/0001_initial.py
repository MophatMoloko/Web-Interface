# Generated by Django 4.1 on 2022-08-14 19:31

from django.db import migrations, models
import incidents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('upload', models.FileField(upload_to='uploads/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]