# Generated by Django 2.2.12 on 2020-04-09 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_test"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="test",),
    ]