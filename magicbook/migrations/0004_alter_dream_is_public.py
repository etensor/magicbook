# Generated by Django 4.1 on 2022-11-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magicbook", "0003_remove_dream_titulo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dream",
            name="is_public",
            field=models.BooleanField(default=True),
        ),
    ]