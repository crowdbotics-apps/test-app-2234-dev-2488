# Generated by Django 2.2.12 on 2020-04-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_customtext_test"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="test",),
    ]