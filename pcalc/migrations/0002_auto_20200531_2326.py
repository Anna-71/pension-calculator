# Generated by Django 2.2.12 on 2020-05-31 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcalc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pcalc_info',
            name='army',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='child',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='other',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='pensia',
            field=models.CharField(default='0', max_length=40),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='stl1',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='stl2',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='stn1',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='stn2',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='sv',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='szar14',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='szar15',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='szar2',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='pcalc_info',
            name='szar5',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
