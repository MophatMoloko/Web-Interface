# Generated by Django 4.1 on 2022-09-14 23:05

from django.db import migrations, models
import tkinter.tix


class Migration(migrations.Migration):

    dependencies = [
        ('studentResults', '0007_rename_assignmentfive_student_assignment1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentNumber',
            field=models.CharField(default='No Value', max_length=3, primary_key=tkinter.tix.Tree, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='testAverage',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
