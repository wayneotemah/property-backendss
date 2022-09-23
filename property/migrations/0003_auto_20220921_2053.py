# Generated by Django 3.2.13 on 2022-09-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20220919_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='number_of_units',
        ),
        migrations.AddField(
            model_name='property',
            name='city',
            field=models.CharField(default='Nairobi', max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='zipcode',
            field=models.PositiveBigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residentailproperty',
            name='beds',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='residentailproperty',
            name='square_feet',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
