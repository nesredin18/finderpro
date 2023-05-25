# Generated by Django 4.2 on 2023-05-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0005_found_i_item_type_lost_i_matched_p_matched_i_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='found_i',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='found_p',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lost_i',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lost_p',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='matched_i',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='matched_p',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='wanted_p',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]