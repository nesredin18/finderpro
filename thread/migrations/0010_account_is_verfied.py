# Generated by Django 4.2 on 2023-05-23 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0009_alter_account_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verfied',
            field=models.BooleanField(default=False),
        ),
    ]
