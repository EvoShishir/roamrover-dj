# Generated by Django 5.0.6 on 2024-06-04 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_locationcost_distance_alter_locationcost_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
