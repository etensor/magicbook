# Generated by Django 4.1 on 2022-11-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magicbook", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="password",
            field=models.CharField(max_length=128, verbose_name="Password"),
        ),
    ]