# Generated by Django 2.2.16 on 2020-10-05 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodstypemenu',
            old_name='type',
            new_name='types',
        ),
    ]