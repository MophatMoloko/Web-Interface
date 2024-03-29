# Generated by Django 4.1 on 2022-09-08 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor_Marking',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('A1_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
                ('A2_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
                ('A3_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
                ('A4_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
                ('A5_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
                ('A6_Marker', models.CharField(choices=[('default tutor', 'Tutor is default'), ('BNDJAM007', 'Tutor is default'), ('TRMDON002', 'Tutor is default'), ('JHNBOR002', 'Tutor is default'), ('MNDNEL001', 'Tutor is default'), ('ZMXJAC003', 'Tutor is default'), ('RMPCYR004', 'Tutor is default'), ('NHXTRE001', 'Tutor is default'), ('RBNNIC005', 'Tutor is default'), ('LTTMAR002', 'Tutor is default'), ('PWRAUS003', 'Tutor is default'), ('MBKTHA002', 'Tutor is default'), ('CRRJIM004', 'Tutor is default'), ('JHNBOR002', 'Tutor is default')], default='default tutor', max_length=15)),
            ],
        ),
    ]
