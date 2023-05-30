# Generated by Django 4.2 on 2023-05-30 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repo',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='repo',
            name='repo_n',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='repo',
            name='reported',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offender_reported', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repo',
            name='reporter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='offended_reporter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='reponumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_n', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now=True)),
                ('reported', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='count_reported', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
