# Generated by Django 4.2 on 2023-05-30 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0013_alter_account_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matched_p',
            name='found_id',
        ),
        migrations.RemoveField(
            model_name='matched_p',
            name='lost_id',
        ),
        migrations.DeleteModel(
            name='matched_i',
        ),
        migrations.DeleteModel(
            name='matched_p',
        ),
    ]
