# Generated by Django 3.2.13 on 2024-01-26 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0009_auto_20220512_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourceassistancetransaction',
            old_name='cfda_number',
            new_name='assistance_listing_number',
        ),
        migrations.RenameField(
            model_name='sourceassistancetransaction',
            old_name='cfda_title',
            new_name='assistance_listing_title',
        ),
    ]