# Generated by Django 4.1 on 2022-09-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentResults', '0002_alter_student_assignmentaverage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='assignmentAverage',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentFive',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentFour',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentOne',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentSix',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentThree',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='assignmentTwo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='finalMark',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='testAverage',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='testOne',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='testTwo',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
