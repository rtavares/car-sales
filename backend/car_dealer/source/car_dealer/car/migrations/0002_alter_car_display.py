# Generated by Django 5.1.1 on 2024-10-06 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("car", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="display",
            field=models.BooleanField(default=False),
        ),
    ]
