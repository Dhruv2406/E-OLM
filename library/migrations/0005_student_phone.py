# Generated by Django 3.1.7 on 2021-08-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20210827_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
