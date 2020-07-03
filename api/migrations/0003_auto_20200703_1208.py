# Generated by Django 3.0.7 on 2020-07-03 10:08

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200703_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackableitem',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 10, 8, 50, 77187, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trackableitem',
            name='trackable_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.TrackableItem'),
        ),
    ]