# Generated by Django 5.0.3 on 2024-03-30 22:43

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'University', 'verbose_name_plural': 'Universities'},
        ),
        migrations.AddField(
            model_name='university',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='university',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
