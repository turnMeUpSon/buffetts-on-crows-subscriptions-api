# Generated by Django 5.0.2 on 2024-02-26 21:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription_service', '0002_plan_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.localtime),
        ),
    ]
