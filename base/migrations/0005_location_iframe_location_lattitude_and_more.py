# Generated by Django 5.0.6 on 2024-06-04 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_location_acrophobic_location_cautious_location_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='iframe',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='lattitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='overview',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
