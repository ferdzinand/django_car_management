# Generated by Django 2.2.11 on 2023-06-11 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0005_auto_20230611_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='car',
            name='position',
            field=models.FloatField(default=0, max_length=50),
        ),
    ]
