# Generated by Django 2.2.11 on 2020-04-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0006_auto_20200405_0001"),
    ]

    operations = [
        migrations.AlterField(
            model_name="healthentry",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="M", max_length=1
            ),
        ),
    ]