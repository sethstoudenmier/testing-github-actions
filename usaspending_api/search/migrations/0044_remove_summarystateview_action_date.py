# Generated by Django 3.2.25 on 2024-09-04 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0043_add_total_outlays_summary_state_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summarystateview',
            name='action_date',
        ),
    ]