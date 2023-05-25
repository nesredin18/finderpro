# Generated by Django 4.2 on 2023-05-02 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0002_user_type_account_adress_account_p_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='person_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='wanted_p',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_n', models.CharField(max_length=100)),
                ('last_n', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('cloth', models.TextField()),
                ('mark', models.TextField()),
                ('detail', models.TextField()),
                ('reason', models.TextField()),
                ('adress', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lost_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_n', models.CharField(max_length=100)),
                ('last_n', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('cloth', models.TextField()),
                ('mark', models.TextField()),
                ('detail', models.TextField()),
                ('adress', models.CharField(max_length=100)),
                ('p_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thread.person_type')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='found_P',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_n', models.CharField(max_length=100)),
                ('last_n', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('cloth', models.TextField()),
                ('mark', models.TextField()),
                ('detail', models.TextField()),
                ('adress', models.CharField(max_length=100)),
                ('p_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='thread.person_type')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
