# Generated by Django 5.1.1 on 2024-11-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0003_event_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/%Y/%m/%d/events"
            ),
        ),
    ]