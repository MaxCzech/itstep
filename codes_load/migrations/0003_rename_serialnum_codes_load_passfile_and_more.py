# Generated by Django 4.2.4 on 2023-12-11 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codes_load', '0002_alter_codes_load_serialnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codes_load',
            old_name='serialNum',
            new_name='passFile',
        ),
        migrations.RemoveField(
            model_name='codes_load',
            name='code',
        ),
    ]
