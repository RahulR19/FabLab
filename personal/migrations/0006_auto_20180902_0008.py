# Generated by Django 2.0.5 on 2018-09-01 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20180901_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Instrument',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='item',
            name='Rollno',
            field=models.CharField(max_length=10),
        ),
    ]