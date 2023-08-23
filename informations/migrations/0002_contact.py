# Generated by Django 4.2 on 2023-06-22 21:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('informations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, default='question', null=True)),
                ('asker', models.EmailField(blank=True, default='email', max_length=100, null=True)),
                ('answer', models.TextField(blank=True, default='answer', null=True)),
                ('answerer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answerer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]